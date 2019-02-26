from datetime import datetime, timedelta
import sqlite3

from helpers import create_db, db_open, db_close, login_required, time_now

# headache reporting related functions

def report_headache(session, form_data):
    """ Reports a new headache """
    # create empty dict for data
    data = {}

# set date and start_time field
    # get current date and time
    current_datetime = time_now()

    # if given time is earlier
    if form_data['_time'] != 'now':
        # check whether munites or hours have passed
        # and make necessary changes to current_datetime
        if form_data['_time_unit'] == 'minutes':
            current_datetime -= timedelta(minutes=int(form_data['_time_passed']))
        else:
            # only one other possibility
            current_datetime -= timedelta(hours=int(form_data['_time_passed']))

    # set date and start_time field values
    data['date'] = current_datetime.strftime("%Y-%m-%d")
    data['start_time'] = current_datetime.strftime("%H:%M:%S")

    # set medication value to medictaion taken (dosage)
    if form_data['_medication_taken'] == 'yes':
        meds_name = form_data['_medication_name'].strip().title()
        meds_dose = form_data['_medication_dose'].replace(" ", "")
        data['medication'] = f"{meds_name} ({meds_dose})"
        data['medication_effect'] = form_data['_medication_effect']

        # if medication helped, mark headache as resolved
        if data['medication_effect'] == 'resolved headache':
            data['duration'] = str(time_now() - current_datetime)[:4]

    # add data submitted through form to dict
    for k, v in form_data.items():
        # skip send button (name starts with '_')
        if not k.startswith('_'):
            # parse data from checkboxes
            if '.' in k:
                db_key, db_value = k.split('.')
            # parse data from text fields and radios
            else:
                db_key, db_value = k, v.strip().replace('_', ' ')


            # add multiple values, if given
            if db_key in data:
                data[db_key] += f"; {db_value.replace('_', ' ')}"
            else:
                data[db_key] = db_value.replace('_', ' ')


    # create SQL strings of database table fields and values from user input given
    for key in data:
        # create variables and add first column name
        if 'cols' not in locals():
            cols = str(key)
            values = f":{str(key)}"
        # add the rest of the table names to the strings
        else:
            cols += f", {str(key)}"
            values += f", :{str(key)}"

    # update database
    db, cur = db_open()
    cur.execute(f"INSERT INTO {session['user_table']} ({cols}) VALUES ({values})", data)
    db_close(db)


def update_headache(session, form_data):
    """ Updates an unresolved headache """
    # create empty dict for data
    data = {}

    # if headache has been resolved
    if form_data['_resolved'] == 'yes':
    # time related
        current_datetime = time_now()
        # combine and convert date and start_time strings to datetime object
        start_time = datetime.strptime(form_data['_start_time'], "%Y-%m-%d %H:%M:%S")

        # check when pain stopped
        if form_data['_time'] != 'now':
            # check whether minutes or hours have passed
            # and make necessary changes to current_datetime
            if form_data['_time_unit'] == 'minutes':
                current_datetime -= timedelta(minutes=int(form_data['_time_passed']))
            else:
                # only one other possibility
                current_datetime -= timedelta(hours=float(form_data['_time_passed']))

        # check whether a valid time was given, before assigning value to data['duration']
        # an invalid date would not store the headache as resolved, but all other values would be stored
        # TODO this still needs some work, eg error message of some sort
        if current_datetime > start_time:
            duration = (current_datetime - start_time)
            data['duration'] = str(duration)[:4]

    # meds related
        # determining a possible solution causing resolution of headache
        # 1. medication was taken previously
        if '_prev_medication' in form_data:

            # 1.1 check whether more medication was taken
            if form_data['_medication_taken'] == 'yes':
                # in this case, we assume that the last taken meds resolved the headache
                # the previous meds are kept in the database, as it could have been a combination
                # of all meds taken
                data['medication'] = f"{form_data['_prev_medication']}; {form_data['_medication_name']}" + \
                        f"({form_data['_medication_dose']})"

                if form_data['_prev_medication_effect'].endswith("too early"):
                    # handle previously added medication effects
                    # create list of previous effects
                    prev_effect = form_data['_prev_medication'].split("; ")
                    # change last effect to unknown
                    prev_effect[-1] = "unknown"
                    # create string from list
                    data['medication_effect'] = "; ".join(prev_effect)

                # add successful result
                data['medication_effect'] += "; resolved headache"

            else:
                # if no other meds have been taken, we assume the last meds taken did the trick
                prev_effect = form_data['_prev_medication_effect'].split("; ")
                # change last effect to successful result
                prev_effect[-1] = "resolved headache"
                # create string from list
                data['medication_effect'] = "; ".join(prev_effect)

        # 2. no meds were taken earlier
        # check whether med were taken now
        elif form_data['_medication_taken'] == 'yes':
            # store medication name and dose and that it resolved the headache
            data['medication'] = f"{form_data['_medication_name']} ({form_data['_medication_dose']})"
            data['medication_effect'] = "resolved headache"


    # if headache is still present
    else:
        # check if medication was taken previously and update its effect in database
        if '_prev_medication' in form_data:

            data['medication'] = form_data['_prev_medication']

            if form_data['_prev_medication_effect'].endswith("too early"):
                # handle previously added medication effects
                # create list of previous effects
                prev_effect = form_data['_prev_medication'].split("; ")
                # update last effect
                prev_effect[-1] = form_data['_updated_medication_effect']
                # create a string from list
                data['medication_effect'] = "; ".join(prev_effect)
            else:
                data['medication_effect'] = form_data['_prev_medication_effect']

            # check if more medication has been taken
            if form_data['_medication_taken'] == 'yes':

                data['medication'] = f"{form_data['_prev_medication']}; {form_data['_medication_name']}" + \
                        f"({form_data['_medication_dose']})"
                data['medication_effect'] += f"; {form_data['_medication_effect']}"


        elif form_data['_medication_taken'] == 'yes':

            data['medication'] = f"{form_data['_medication_name']} ({form_data['_medication_dose']})"
            data['medication_effect'] = f"; {form_data['_medication_effect']}"

    if form_data['comments'].strip():
        data['comments'] = form_data['comments'].strip()

    if form_data['routine_disruption'].strip():
        data['routine_disruption'] = form_data['routine_disruption'].strip()

    if data:
        # set update string variable
        update = ""
        # add fieldnames and values
        for k, v in data.items():
                update += f"{k} = '{v}', "
        # remove last comma
        update = update[:-2]

        # update database
        db, cur = db_open()
        cur.execute(f"UPDATE {session['user_table']} SET {update} WHERE id = {form_data['_id']}")
        db_close(db)
