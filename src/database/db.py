from src.database.config import supabase
import bcrypt



def hash_pass(pwd):
    return bcrypt.hashpw(pwd.encode(), bcrypt.gensalt()).decode()

def check_pass(pwd, hashed):
    return bcrypt.checkpw(pwd.encode(), hashed.encode())


def check_teacher_exists(username):
    # Check for unique username, returns false when username is already taken
    response = supabase.table("teachers").select("username").eq("username", username).execute()
    return len(response.data) > 0 

def create_teacher(username, password, name):

    data = { "username" : username, "password": hash_pass(password), "name": name}
    response = supabase.table("teachers").insert(data).execute()
    return response.data


def teacher_login(username, password):
    response = supabase.table("teachers").select("*").eq("username", username).execute()
    if response.data:
        teacher = response.data[0]
        if check_pass(password, teacher['password']):
            return teacher
    return None


def get_all_students():
    response = supabase.table('student').select("*").execute()
    return response.data

def create_student(new_name, face_embeddings=None, voice_embedding=None):
    data = {'name': new_name, 'face_embeddings':face_embeddings, "voice_embedding": voice_embedding}
    response = supabase.table('student').insert(data).execute()
    return response.data


def create_subject(subject_code,name,section,teachers_id):
    data={"subject_code":subject_code,"name":name,"section":section,"teachers_id":teachers_id}
    response=supabase.table("subjects").insert(data).execute()
    return response.data

def get_teacher_subjects(teachers_id):
    response=supabase.table('subjects').select("*,subject_student(count),attendance_box(timestamp)").eq("teachers_id",teachers_id).execute()
    subjects = response.data
    
    for sub in subjects:
        sub['total_student'] = sub.get("subject_student",[{}])[0].get('count',0) if sub.get('subject_student') else 0
        attendance = sub.get('attendance_box',[])
        unique_sessions = len(set(log['timestamp'] for log in attendance))
        sub['total_classes'] = unique_sessions

    return subjects

def  enroll_student_to_subject(student_id, subject_id):
    data = {'student_id': student_id, "subject_id": subject_id}
    response= supabase.table('subject_student').insert(data).execute()
    return response.data


def  unenroll_student_to_subject(student_id, subject_id):
    response= supabase.table('subject_student').delete().eq('student_id', student_id).eq('subject_id', subject_id).execute()
    return response.data



def get_student_subjects(student_id):
    response = supabase.table('subject_student').select('*, subjects(*)').eq('student_id', student_id).execute()
    return response.data


def get_student_attendance(student_id):
    response = supabase.table('attendance_box').select('*, subjects(*)').eq('student_id', student_id).execute()
    return response.data

def create_attendance(logs):
    response = supabase.table('attendance_box').insert(logs).execute()
    return response.data

def get_attendance_for_teacher(teachers_id):
    response = supabase.table('attendance_box').select("*, subjects!inner(*)").eq('subjects.teachers_id', teachers_id).execute()
    return response.data