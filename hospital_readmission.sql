-- patients table
create table patients(
    patient_id serial primary key,
    first_name varchar(50),
    last_name varchar(50),
    gender varchar(50),
    date_of_birth date
);

-- admissions table
create table admissions(
    admission_id serial primary key,
    patient_id int references patients(patient_id),
    admission_date date,
    discharge_date date,
    readmitted boolean,
    length_of_stay int generated always as (discharge_date - admission_date) stored
);

-- diagnoses table
create table diagnoses (
    diagnosis_id serial primary key,
    admission_id int references admissions(admission_id),
    diagnosis_code varchar(20),
    description text
);

-- create procedures
create table procedures (
    procedure_id serial primary key,
    admission_id int references admissions(admission_id),
    procedure_code varchar(20),
    description text
);

-- create medications
create table medications (
    medication_id serial primary key,
    admission_id int references admissions(admission_id),
    medication_name varchar(100),
    dosage varchar(50),
    frequency varchar(50)
);

-- create doctors
create table doctors (
    doctor_id serial primary key,
    first_name varchar(50),
    last_name varchar(50),
    specialty varchar(100),
    department varchar(100)
);

-- create admission_doctors
create table admission_doctors(
    admission_id int references admissions(admission_id),
    doctor_id int references doctors (doctor_id),
    role varchar(50),
    primary key (admission_id, doctor_id)
)

-- inserting data
INSERT INTO patients (patient_id, first_name, last_name, gender, date_of_birth) VALUES
(1, 'Stephanie', 'Carter', 'Female', DATE '1988-02-04'),
(2, 'Justin', 'Howard', 'Male', DATE '1966-06-10'),
(3, 'Julie', 'Gonzales', 'Female', DATE '1947-10-16'),
(4, 'Kimberly', 'Boyd', 'Female', DATE '1994-07-27'),
(5, 'Wesley', 'Greer', 'Male', DATE '1947-08-04'),
(6, 'Jacob', 'Reid', 'Male', DATE '1943-03-06'),
(7, 'Jonathan', 'Williams', 'Male', DATE '1976-11-12'),
(8, 'Karen', 'Phillips', 'Female', DATE '1981-07-23'),
(9, 'Jeremy', 'Ford', 'Male', DATE '1970-12-09'),
(10, 'Ashley', 'Allen', 'Female', DATE '1981-03-09'),
(11, 'Sarah', 'Ward', 'Female', DATE '1964-09-01'),
(12, 'Matthew', 'Reed', 'Male', DATE '1973-06-18'),
(13, 'Dustin', 'Walker', 'Male', DATE '1956-07-30'),
(14, 'Michele', 'Martin', 'Female', DATE '1970-12-10'),
(15, 'Mark', 'Keller', 'Male', DATE '1962-02-01'),
(16, 'Dylan', 'Baker', 'Male', DATE '1981-09-06'),
(17, 'Joseph', 'Klein', 'Male', DATE '1958-03-02'),
(18, 'James', 'Robinson', 'Male', DATE '1961-03-01'),
(19, 'Erica', 'Fox', 'Female', DATE '1956-04-18'),
(20, 'Joshua', 'White', 'Male', DATE '1950-12-13');

INSERT INTO doctors (doctor_id, first_name, last_name, specialty, department) VALUES
(1, 'Frank', 'Gray', 'Cardiology', 'Cardiology'),
(2, 'Veronica', 'Bowman', 'Endocrinology', 'Endocrinology'),
(3, 'Angela', 'Cohen', 'Oncology', 'Oncology'),
(4, 'Megan', 'Parsons', 'General Medicine', 'General Medicine'),
(5, 'Jeremy', 'Johnson', 'Pulmonology', 'Pulmonology'),
(6, 'Leslie', 'Adams', 'Pulmonology', 'Pulmonology'),
(7, 'Jason', 'Hahn', 'Endocrinology', 'Endocrinology'),
(8, 'Nancy', 'Edwards', 'Endocrinology', 'Endocrinology'),
(9, 'Diana', 'Foster', 'Pulmonology', 'Pulmonology'),
(10, 'Robin', 'Ellis', 'Cardiology', 'Cardiology'),
(11, 'Joseph', 'Wright', 'Cardiology', 'Cardiology'),
(12, 'Anna', 'Baker', 'General Medicine', 'General Medicine'),
(13, 'Brenda', 'Hurst', 'Cardiology', 'Cardiology'),
(14, 'Reginald', 'Robinson', 'Pulmonology', 'Pulmonology'),
(15, 'Whitney', 'Hicks', 'Pulmonology', 'Pulmonology'),
(16, 'Christopher', 'Williams', 'Neurology', 'Neurology'),
(17, 'Daniel', 'Burton', 'Pulmonology', 'Pulmonology'),
(18, 'Laura', 'Henderson', 'Cardiology', 'Cardiology'),
(19, 'Bryan', 'James', 'Oncology', 'Oncology'),
(20, 'Wendy', 'Rice', 'General Medicine', 'General Medicine');

INSERT INTO admissions (patient_id, admission_date, discharge_date, readmitted) VALUES
(1, '2023-01-10', '2023-01-15', FALSE),
(2, '2023-02-05', '2023-02-10', TRUE),
(3, '2023-02-20', '2023-02-28', FALSE),
(4, '2023-03-05', '2023-03-10', TRUE),
(5, '2023-03-15', '2023-03-20', FALSE),
(6, '2023-04-01', '2023-04-08', FALSE),
(7, '2023-04-12', '2023-04-17', TRUE),
(8, '2023-04-25', '2023-05-01', FALSE),
(9, '2023-05-10', '2023-05-16', TRUE),
(10, '2023-05-20', '2023-05-26', FALSE),
(11, '2023-06-01', '2023-06-06', FALSE),
(12, '2023-06-12', '2023-06-17', TRUE),
(13, '2023-06-22', '2023-06-27', FALSE),
(14, '2023-07-01', '2023-07-05', TRUE),
(15, '2023-07-10', '2023-07-15', FALSE),
(16, '2023-07-18', '2023-07-24', TRUE),
(17, '2023-08-01', '2023-08-06', FALSE),
(18, '2023-08-10', '2023-08-15', TRUE),
(19, '2023-08-18', '2023-08-23', FALSE),
(20, '2023-09-01', '2023-09-07', TRUE);

INSERT INTO diagnoses (diagnosis_id, admission_id, diagnosis_code, description) VALUES
(1, 17, 'I21', 'Will seven medical.'),
(2, 3, 'I10', 'That fear.'),
(3, 4, 'E11', 'Participant check several much.'),
(4, 6, 'C50', 'Truth out major born guy.'),
(5, 14, 'F32', 'Dream drive note.'),
(6, 3, 'I21', 'Beat magazine.'),
(7, 13, 'F32', 'Within mouth.'),
(8, 15, 'F32', 'Campaign little near.'),
(9, 9, 'F32', 'Month parent who.'),
(10, 1, 'C50', 'Sense ready require human public.'),
(11, 4, 'C50', 'Just military building different.'),
(12, 18, 'J45', 'Again network open according.'),
(13, 11, 'I10', 'Arrive attack all form method.'),
(14, 10, 'I21', 'Protect Democrat car.'),
(15, 6, 'I21', 'Office drug list imagine behind.'),
(16, 1, 'C50', 'Great in tell approach.'),
(17, 9, 'F32', 'Art rock.'),
(18, 6, 'F32', 'Eat couple.'),
(19, 4, 'C50', 'Cell contain leg themselves.'),
(20, 10, 'C50', 'Kitchen technology.');


INSERT INTO procedures (procedure_id, admission_id, procedure_code, description) VALUES
(1, 17, '70450', 'Better present music.'),
(2, 7, '80050', 'Better.'),
(3, 12, '80050', 'Coach magazine.'),
(4, 18, '70450', 'Ten total.'),
(5, 1, '70450', 'Her world.'),
(6, 11, '92928', 'Unit size.'),
(7, 1, '93010', 'Institution whatever.'),
(8, 12, '93005', 'Product main couple.'),
(9, 8, '93010', 'Why often.'),
(10, 8, '70450', 'Article finish anyone.'),
(11, 3, '93010', 'Me system church.'),
(12, 16, '93010', 'Bag control organization.'),
(13, 18, '80050', 'Identify walk.'),
(14, 5, '12001', 'East organization people.'),
(15, 16, '70450', 'Price north first.'),
(16, 6, '93005', 'Daughter respond.'),
(17, 17, '70450', 'Enter capital.'),
(18, 14, '80050', 'Lead upon.'),
(19, 18, '12001', 'Act perform.'),
(20, 7, '12001', 'You available defense.');


INSERT INTO medications (medication_id, admission_id, medication_name, dosage, frequency) VALUES
(1, 10, 'Aspirin', '348mg', 'As needed'),
(2, 12, 'Aspirin', '465mg', 'As needed'),
(3, 15, 'Lisinopril', '131mg', 'Once daily'),
(4, 3, 'Albuterol', '15mg', 'As needed'),
(5, 18, 'Metformin', '306mg', 'Once daily'),
(6, 1, 'Lisinopril', '367mg', 'As needed'),
(7, 2, 'Metformin', '39mg', 'Once daily'),
(8, 11, 'Lisinopril', '268mg', 'Once daily'),
(9, 9, 'Levothyroxine', '253mg', 'Once daily'),
(10, 18, 'Metformin', '375mg', 'As needed'),
(11, 19, 'Aspirin', '129mg', 'Twice daily'),
(12, 14, 'Metformin', '53mg', 'Once daily'),
(13, 14, 'Albuterol', '221mg', 'Twice daily'),
(14, 15, 'Levothyroxine', '32mg', 'As needed'),
(15, 4, 'Lisinopril', '211mg', 'As needed'),
(16, 11, 'Lisinopril', '132mg', 'Once daily'),
(17, 7, 'Atorvastatin', '234mg', 'Once daily'),
(18, 14, 'Metformin', '147mg', 'Twice daily'),
(19, 8, 'Lisinopril', '231mg', 'As needed'),
(20, 4, 'Lisinopril', '338mg', 'As needed');

INSERT INTO admission_doctors (admission_id, doctor_id, role) VALUES
(1, 3, 'Primary'),
(6, 14, 'Consulting'),
(16, 7, 'Consulting'),
(2, 6, 'Consulting'),
(1, 13, 'Consulting'),
(15, 10, 'Consulting'),
(18, 16, 'Primary'),
(7, 10, 'Primary'),
(2, 19, 'Primary'),
(11, 2, 'Primary'),
(19, 16, 'Primary'),
(2, 17, 'Primary'),
(6, 3, 'Primary'),
(8, 13, 'Primary'),
(19, 8, 'Primary'),
(20, 3, 'Consulting'),
(19, 19, 'Consulting'),
(9, 7, 'Consulting'),
(8, 9, 'Consulting'),
(5, 10, 'Consulting');


-- Basic Exploration Queries
-- Readmission rate
select count (*) filter (where readmitted) * 100.0 / count (*) 
    as readmission_rate_percentage from admissions


-- list all patient and readmission info
create view patient_admission_summary as
select 
    p.patient_id,
    p.first_name || ' ' || p.last_name as full_name,
    d.diagnosis_code,
    d.description as diagnosis_description,
    a.admission_date,
    a.discharge_date,
    a.length_of_stay,
    a.readmitted
from patients p
join admissions a on a.patient_id = p.patient_id
join diagnoses d on a.admission_id  = d.admission_id
order by a.admission_date

select * from patient_admission_summary