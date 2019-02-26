$(document).ready(function(){

    // set behaviour for required fields.
    // below every required field, there should be a div .emptyFieldFeedback
    // which will be hidden and become visible when required field is left empty
    $(".requiredField").change(function(){
        // checkboxes don't have their emptyFieldFeedback divs as siblings,
        // and should therefore be handled differently than text inputs (below).
        if ($(this).is(":checkbox")) {
            if (!$(this).is(":checked")) {
                $(this).parent().siblings(".emptyFieldFeedback").slideDown('fast');
            }
            else {
                $(this).parent().siblings(".emptyFieldFeedback").slideUp();
            }
        }
        else {
            if (!$(this).val()) {
                $(this).siblings(".emptyFieldFeedback").slideDown('fast');
            }
            else {
                $(this).siblings(".emptyFieldFeedback").slideUp();
            }
        }
    });

    // Bootstrap's text-danger classes fade in and out a few times
    $(".text-danger").fadeIn("slow").fadeOut(1500).fadeIn("slow").fadeOut(1500).fadeIn("slow");

    // registration form behaviour and validation
    // create checklist to use for validation of the registration form
    let checklist = {
        birthDayValid: false,
        emailValid: false,
        emailAvailable: false,
        usernameAvailable: false,
        passwordsMatch: false,
        checkBirthDate: function(userInput) {
            let currentYear = Number(new Date().getFullYear());
            if (userInput.length != 8 ||
                Number(userInput.slice(0, 4)) > currentYear || Number(userInput.slice(0, 4)) < 1900 ||
                Number(userInput.slice(4, 6)) > 12 || Number(userInput.slice(4, 6)) < 1 ||
                Number(userInput.slice(6, 8)) > 31 || Number(userInput.slice(6, 8)) < 1)
                {
                    this.birthDayValid = false;
                    $("#regBirth").siblings(".invalidFeedback").slideDown('fast');
                }
            else {
                this.birthDayValid = true;
                $("#regBirth").siblings(".invalidFeedback").slideUp();
            }
        },
        // check if email adress entered is valib using regular expressions
        checkEmail: function(userInput) {
            var emailRegEx = /^([\w-\.]+@([\w-]+\.)+[\w-]{2,4})?$/;
            // if input doesn't match the requirements, an error msg slides down
            if(!emailRegEx.test(userInput)) {
                this.emailValid = false;
                $("#regEmail").siblings(".invalidFeedback").slideDown('fast');

            }
            // if the input matches, check whether the email exists on the server
            else {
                this.emailValid = true;
                // hide away error message if present
                $("#regEmail").siblings(".invalidFeedback").slideUp();

                // check whether email exists in database
                // TODO for future version: This should be a a seperate function,
                // checking for username and/or passwords
                $.get("/checkemail/" + userInput, function(data){
                    if (data == "taken") {
                        checklist.emailAvailable = false;
                        $("#regEmail").siblings(".emailExists").slideDown('fast');
                    }
                    else {
                        checklist.emailAvailable = true;
                        $("#regEmail").siblings(".emailExists").slideUp();
                    }
                });
            }
        },
        // check whether username already exists
        // TODO for future version: combine this with email checking in one function
        checkUsername: function(userInput) {
            $.get("/checkusername/" + userInput, function(data){
                if (data == "taken") {
                    checklist.usernameAvailable = false;
                    $("#regUsername").siblings(".invalidFeedback").slideDown('fast');
                }
                else {
                    checklist.usernameAvailable = true;
                    $("#regUsername").siblings(".invalidFeedback").slideUp();
                }
            });
        },
        // check if both passwords entered match
        checkPasswords: function(password1, password2) {
            (password1 == password2) ? this.passwordsMatch = true : this.passwordsMatch = false;
            return this.passwordsMatch;
        },
        // check whether all checks have been done and requirements were met.
        checkAll: function() {
            return (this.birthDayValid &&
                this.emailValid &&
                this.emailAvailable &&
                this.usernameAvailable &&
                this.passwordsMatch
            );
        }
    };

    // Check if all fields are filled and meet their requirements
    $("form").on("submit", function(){
        // reset validation variable
        let empty_fields = false;
        // iterate over all requiredfields
        $(this).find('.requiredField').each(function() {
            // if an empty field is found, slide down its error message
            if (!$(this).val()){
                $(this).siblings(".emptyFieldFeedback").slideDown('fast');
                // mark that there is at least one empty field
                empty_fields = true;
            }
            // check if checkboxes are checked
            else if ($(this).is(":checkbox") && !$(this).is(":checked")){
                $(this).parent().siblings(".emptyFieldFeedback").slideDown('fast');
                empty_fields = true;
            }
        });
        // cancel submission, if empty fields are present
        if (empty_fields) {
            return false;
        }
        if ($(this).hasClass("regForm")) {
            // if current form is the main registration form
            // check whether all required fields meet their specific requirements
            // submit form if all tests pass
            return checklist.checkAll();
        }
    });

    // Check if valid birth date was entered
    $("#regBirth").blur(function(){
        if ($(this).val().trim()){
            checklist.checkBirthDate($(this).val(), function(){
                !checklist.birthDayValid ? $(this).siblings(".invalidFeedback").slideDown('fast') : $(this).siblings(".invalidFeedback").slideUp();
            });
        }
        else { $(this).siblings(".invalidFeedback").slideUp(); }
    });
    // TODO for future version: the following checks can be done using one function
    // Check if entered email is a valid address
    $("#regEmail").change(function(){
        if ($(this).val().trim()) {
            checklist.checkEmail($(this).val().trim());
        }
        else {
            $("#regEmail").siblings(".emailExists").slideUp();
            $("#regEmail").siblings(".invalidFeedback").slideUp();
        }
    });

    // Check if username is available
    $("#regUsername").change(function(){
        if ($(this).val().trim()) {
            checklist.checkUsername($(this).val().trim());
        }
        else { $(this).siblings(".invalidFeedback").slideUp(); }
    });

    // Check if passwords match
    $("#regPwd2").keyup(function(){
        let match = null;
        if ($("#regPwd").val().trim()){
            match = checklist.checkPasswords($(this).val(), $("#regPwd").val());
        }
        match ? $(this).attr("class", "form-control text-success") : $(this).attr("class", "form-control text-danger");
    });

    // slides down the terms and conditions
    $("#termsCondsSlider").click(function(){
        $("#termsConds").slideDown(1000);
    });


    // Submit headache form functions

    // focus on input field when its check/radio box is checked
    // add class otherField input field element
    $("input.otherField").prev().change(function(){
        if ($(this).is(":checked")) {
            $(this).next().focus();
        }
    });

    $("input.otherField").focus(function() {
        if (!$(this).prev().is(":checked")) {
            $(this).prev().prop("checked", true);
        }
    });

    // set the value of radio/checkbox to that from input field value
    $("input.otherField").change(function() {
       if ($(this).val()) {
           $(this).prev().val($(this).val());
       }
    });

    // time passed selector
    $(".timeUnit").change(function(){
        // set limits for minute field
        if ($(this).val() == 'minutes') {
            $(".timePassed").attr({
                "min": 15,
                "max": 105,
                "step": 15,
                "value": 15
            });
            $(".timePassed").val(15);
        }
        // set limits for hour field
        else {
            $(".timePassed").attr({
                "min": 1,
                "max": 18,
                "step": 1,
            });
            $(".timePassed").val(1);
        }
        $(this).prev(".otherField").focus();
    });


    // intensity range selector
    $("#intensity_slider").change(function() {
        let intensity_scale = ['very light', 'light', 'mild', 'strong', 'very strong'];
        $("#_intensity_value").html(intensity_scale[$(this).val() - 1]);
        $("#intensity").val(intensity_scale[$(this).val() - 1]);
    });


    // sliding of optional form elements
    // https://stackoverflow.com/questions/19821164/jquery-slidedown-slideup-when-radiobutton-is-clicked

    // report_headache.html
    $("input[name=_medication_taken]").change(function(){
        if ($(this).val() == "yes"){
            $("#_medication").slideDown("fast");
        }
        else {
            $("#_medication").slideUp("fast");
        }
    });

    $("input[name=_time]").change(function(){
        if ($(this).val() == "other"){
            $("#_routine").slideDown("fast");
            $("#_medication_choice").slideDown("fast");
        }
        else {
            $("#_routine").slideUp("fast");
            $("#_medication_choice").slideUp("fast");
        }
    });


    // update_headache.html

    $("input[name=_resolved]").change(function(){
        // headache has ended
        if ($(this).val() == "yes"){
            $("#_resolved_time").slideDown("fast");
            $("#_meds_update").slideUp("fast");
            $("._meds_effect").slideUp("fast");

        }
        // headache is still present
        else {
            $("#_resolved_time").slideUp("fast");
            $("#_meds_update").slideDown("fast");
            $("._meds_effect").slideDown("fast");
        }
    });
});
