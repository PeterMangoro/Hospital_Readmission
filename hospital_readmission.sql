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
