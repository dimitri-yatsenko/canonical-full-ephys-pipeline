from my_project import subject

# ========== Insert new "Subject" ===========

subjects = [{'subject': 'dl36', 'sex': 'F', 'subject_birth_date': '2019-05-06 03:20:01'},
            {'subject': 'dl40', 'sex': 'M', 'subject_birth_date': '2019-07-09 03:20:01'},
            {'subject': 'dl56', 'sex': 'F', 'subject_birth_date': '2019-12-11 03:20:01'},
            {'subject': 'dl59', 'sex': 'F', 'subject_birth_date': '2019-03-16 03:20:01'},
            {'subject': 'dl62', 'sex': 'M', 'subject_birth_date': '2019-05-26 03:20:01'},
            {'subject': 'SC011', 'sex': 'M', 'subject_birth_date': '2019-01-06 03:20:01'},
            {'subject': 'SC017', 'sex': 'M', 'subject_birth_date': '2019-08-01 03:20:01'},
            {'subject': 'SC022', 'sex': 'M', 'subject_birth_date': '2019-09-02 03:20:01'},
            {'subject': 'SC030', 'sex': 'F', 'subject_birth_date': '2019-10-19 03:20:01'},
            {'subject': 'SC031', 'sex': 'F', 'subject_birth_date': '2019-12-11 03:20:01'},
            {'subject': 'SC035', 'sex': 'F', 'subject_birth_date': '2019-02-16 03:20:01'},
            {'subject': 'SC038', 'sex': 'F', 'subject_birth_date': '2019-04-26 03:20:01'}]

subject.Subject.insert(subjects, skip_duplicates=True)
