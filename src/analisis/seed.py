# seed.py
# Autor: Pedro Zamora (Líder Grupo 8)
# Descripción: Carga datos ficticios a la API en Render automáticamente

import requests

BASE_URL = 'https://prueba-con-render.onrender.com'

# ─────────────────────────────────────────────
# DATOS
# ─────────────────────────────────────────────

teachers = [
    { "teacherName": "Carlos Mendoza",  "email": "c.mendoza@cesde.edu.co" },
    { "teacherName": "Lucía Herrera",   "email": "l.herrera@cesde.edu.co" },
    { "teacherName": "Andrés Ríos",     "email": "a.rios@cesde.edu.co"    },
    { "teacherName": "Sandra Molina",   "email": "s.molina@cesde.edu.co"  },
    { "teacherName": "Julián Ospina",   "email": "j.ospina@cesde.edu.co"  },
]

subjects = [
    { "subjectName": "Matemáticas",      "description": "Cálculo y álgebra lineal"               },
    { "subjectName": "Programación",     "description": "Fundamentos de programación en Java"    },
    { "subjectName": "Base de Datos",    "description": "Modelado y consultas SQL"               },
    { "subjectName": "Inglés",           "description": "Inglés técnico nivel B1"                },
    { "subjectName": "Redes",            "description": "Fundamentos de redes y protocolos"      },
    { "subjectName": "Algoritmos",       "description": "Diseño y análisis de algoritmos"        },
    { "subjectName": "Estadística",      "description": "Estadística descriptiva e inferencial"  },
    { "subjectName": "Ética Profesional","description": "Ética y responsabilidad en ingeniería"  },
]

students = [
    { "studentName": "Valentina Torres",  "email": "v.torres@cesde.edu.co",  "document": "1023456781" },
    { "studentName": "Sebastián Gómez",   "email": "s.gomez@cesde.edu.co",   "document": "1023456782" },
    { "studentName": "Mariana López",     "email": "m.lopez@cesde.edu.co",   "document": "1023456783" },
    { "studentName": "Kevin Ramírez",     "email": "k.ramirez@cesde.edu.co", "document": "1023456784" },
    { "studentName": "Didier Castillo",   "email": "d.castillo@cesde.edu.co","document": "1023456785" },
    { "studentName": "Camila Vargas",     "email": "c.vargas@cesde.edu.co",  "document": "1023456786" },
    { "studentName": "Juan Pérez",        "email": "j.perez@cesde.edu.co",   "document": "1023456787" },
    { "studentName": "Luisa Mora",        "email": "l.mora@cesde.edu.co",    "document": "1023456788" },
    { "studentName": "Andrés Cárdenas",   "email": "a.cardenas@cesde.edu.co","document": "1023456789" },
    { "studentName": "Natalia Sierra",    "email": "n.sierra@cesde.edu.co",  "document": "1023456790" },
    { "studentName": "Felipe Gutiérrez",  "email": "f.gutierrez@cesde.edu.co","document": "1023456791"},
    { "studentName": "Sara Bedoya",       "email": "s.bedoya@cesde.edu.co",  "document": "1023456792" },
    { "studentName": "Mateo Restrepo",    "email": "m.restrepo@cesde.edu.co","document": "1023456793" },
    { "studentName": "Isabella Ríos",     "email": "i.rios@cesde.edu.co",    "document": "1023456794" },
    { "studentName": "Santiago Muñoz",    "email": "s.munoz@cesde.edu.co",   "document": "1023456795" },
]

grades_template = [
    { "value": 4.5, "period": "2024-1", "registrationDate": "2024-02-10", "student": 1,  "subject": 1, "teacher": 1 },
    { "value": 3.8, "period": "2024-1", "registrationDate": "2024-02-11", "student": 1,  "subject": 2, "teacher": 2 },
    { "value": 2.5, "period": "2024-1", "registrationDate": "2024-02-12", "student": 1,  "subject": 3, "teacher": 3 },
    { "value": 4.9, "period": "2024-1", "registrationDate": "2024-02-13", "student": 2,  "subject": 1, "teacher": 1 },
    { "value": 1.8, "period": "2024-1", "registrationDate": "2024-02-14", "student": 2,  "subject": 4, "teacher": 4 },
    { "value": 3.2, "period": "2024-1", "registrationDate": "2024-02-15", "student": 3,  "subject": 2, "teacher": 2 },
    { "value": 4.1, "period": "2024-1", "registrationDate": "2024-02-16", "student": 3,  "subject": 5, "teacher": 5 },
    { "value": 3.5, "period": "2024-1", "registrationDate": "2024-02-17", "student": 4,  "subject": 3, "teacher": 3 },
    { "value": 2.9, "period": "2024-1", "registrationDate": "2024-02-18", "student": 4,  "subject": 6, "teacher": 1 },
    { "value": 4.7, "period": "2024-1", "registrationDate": "2024-02-19", "student": 5,  "subject": 1, "teacher": 1 },
    { "value": 1.5, "period": "2024-2", "registrationDate": "2024-08-10", "student": 5,  "subject": 7, "teacher": 4 },
    { "value": 3.9, "period": "2024-2", "registrationDate": "2024-08-11", "student": 6,  "subject": 2, "teacher": 2 },
    { "value": 4.3, "period": "2024-2", "registrationDate": "2024-08-12", "student": 6,  "subject": 8, "teacher": 5 },
    { "value": 2.1, "period": "2024-2", "registrationDate": "2024-08-13", "student": 7,  "subject": 3, "teacher": 3 },
    { "value": 3.6, "period": "2024-2", "registrationDate": "2024-08-14", "student": 7,  "subject": 5, "teacher": 5 },
    { "value": 4.8, "period": "2024-2", "registrationDate": "2024-08-15", "student": 8,  "subject": 1, "teacher": 1 },
    { "value": 3.0, "period": "2024-2", "registrationDate": "2024-08-16", "student": 8,  "subject": 4, "teacher": 4 },
    { "value": 4.2, "period": "2024-2", "registrationDate": "2024-08-17", "student": 9,  "subject": 6, "teacher": 1 },
    { "value": 2.7, "period": "2024-2", "registrationDate": "2024-08-18", "student": 9,  "subject": 2, "teacher": 2 },
    { "value": 3.4, "period": "2024-2", "registrationDate": "2024-08-19", "student": 10, "subject": 7, "teacher": 4 },
    { "value": 4.6, "period": "2025-1", "registrationDate": "2025-02-10", "student": 10, "subject": 1, "teacher": 1 },
    { "value": 1.9, "period": "2025-1", "registrationDate": "2025-02-11", "student": 11, "subject": 3, "teacher": 3 },
    { "value": 3.7, "period": "2025-1", "registrationDate": "2025-02-12", "student": 11, "subject": 8, "teacher": 5 },
    { "value": 4.4, "period": "2025-1", "registrationDate": "2025-02-13", "student": 12, "subject": 2, "teacher": 2 },
    { "value": 2.3, "period": "2025-1", "registrationDate": "2025-02-14", "student": 12, "subject": 5, "teacher": 5 },
    { "value": 4.0, "period": "2025-1", "registrationDate": "2025-02-15", "student": 13, "subject": 4, "teacher": 4 },
    { "value": 3.3, "period": "2025-1", "registrationDate": "2025-02-16", "student": 13, "subject": 6, "teacher": 1 },
    { "value": 4.5, "period": "2025-1", "registrationDate": "2025-02-17", "student": 14, "subject": 1, "teacher": 1 },
    { "value": 1.6, "period": "2025-1", "registrationDate": "2025-02-18", "student": 14, "subject": 7, "teacher": 4 },
    { "value": 3.8, "period": "2025-1", "registrationDate": "2025-02-19", "student": 15, "subject": 3, "teacher": 3 },
    { "value": 4.9, "period": "2025-1", "registrationDate": "2025-02-20", "student": 15, "subject": 8, "teacher": 5 },
]

attendance_template = [
    { "date": "2024-02-10", "status": "PRESENTE",  "student": 1,  "subject": 1 },
    { "date": "2024-02-10", "status": "AUSENTE",   "student": 2,  "subject": 1 },
    { "date": "2024-02-10", "status": "PRESENTE",  "student": 3,  "subject": 1 },
    { "date": "2024-02-11", "status": "TARDANZA",  "student": 1,  "subject": 2 },
    { "date": "2024-02-11", "status": "PRESENTE",  "student": 4,  "subject": 2 },
    { "date": "2024-02-12", "status": "AUSENTE",   "student": 5,  "subject": 3 },
    { "date": "2024-02-12", "status": "PRESENTE",  "student": 6,  "subject": 3 },
    { "date": "2024-08-10", "status": "PRESENTE",  "student": 7,  "subject": 4 },
    { "date": "2024-08-10", "status": "TARDANZA",  "student": 8,  "subject": 4 },
    { "date": "2024-08-11", "status": "PRESENTE",  "student": 9,  "subject": 5 },
    { "date": "2024-08-11", "status": "AUSENTE",   "student": 10, "subject": 5 },
    { "date": "2025-02-10", "status": "PRESENTE",  "student": 11, "subject": 6 },
    { "date": "2025-02-10", "status": "PRESENTE",  "student": 12, "subject": 6 },
    { "date": "2025-02-11", "status": "TARDANZA",  "student": 13, "subject": 7 },
    { "date": "2025-02-11", "status": "AUSENTE",   "student": 14, "subject": 7 },
    { "date": "2025-02-12", "status": "PRESENTE",  "student": 15, "subject": 8 },
]

# ─────────────────────────────────────────────
# FUNCIÓN GENÉRICA DE CARGA
# ─────────────────────────────────────────────

def cargar(endpoint, registros, nombre):
    """Hace POST de cada registro y retorna lista de IDs creados."""
    print(f"\n📤 Cargando {nombre}...")
    ids = []
    for i, dato in enumerate(registros, 1):
        response = requests.post(f'{BASE_URL}/{endpoint}', json=dato)
        if response.status_code == 200:
            id_creado = response.json().get('id')
            ids.append(id_creado)
            print(f"   ✅ {nombre} {i}/{len(registros)} → id={id_creado}")
        else:
            print(f"   ❌ {nombre} {i} falló → {response.status_code}: {response.text}")
            ids.append(None)
    return ids

# ─────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────

if __name__ == '__main__':
    print("🚀 Iniciando carga de datos ficticios en Render...\n")
    print(f"   URL: {BASE_URL}")
    print("=" * 55)

    # 1. Teachers
    ids_teachers = cargar('api/teachers', teachers, 'Teacher')

    # 2. Subjects
    ids_subjects = cargar('api/subjects', subjects, 'Subject')

    # 3. Students
    ids_students = cargar('api/students', students, 'Student')

    # 4. Grades — reemplaza índices por IDs reales devueltos por la API
    grades = []
    for g in grades_template:
        id_student = ids_students[g['student'] - 1]
        id_subject = ids_subjects[g['subject'] - 1]
        id_teacher = ids_teachers[g['teacher'] - 1]

        if id_student and id_subject and id_teacher:
            grades.append({
                "value":            g['value'],
                "period":           g['period'],
                "registrationDate": g['registrationDate'],
                "student":  {"id": id_student},
                "subject":  {"id": id_subject},
                "teacher":  {"id": id_teacher},
            })

    cargar('api/grades', grades, 'Grade')

    # 5. Attendance
    attendance = []
    for a in attendance_template:
        id_student = ids_students[a['student'] - 1]
        id_subject = ids_subjects[a['subject'] - 1]

        if id_student and id_subject:
            attendance.append({
                "date":    a['date'],
                "status":  a['status'],
                "student": {"id": id_student},
                "subject": {"id": id_subject},
            })

    cargar('api/attendance', attendance, 'Attendance')

    print("\n" + "=" * 55)
    print("✅ Carga completa en Render")
    print(f"   Teachers   : {len(ids_teachers)}")
    print(f"   Subjects   : {len(ids_subjects)}")
    print(f"   Students   : {len(ids_students)}")
    print(f"   Grades     : {len(grades)}")
    print(f"   Attendance : {len(attendance)}")



# Pega esto al final de seed.py después del print de cierre

print("\n🔍 Verificando datos en Render...")
for endpoint, nombre in [
    ('api/teachers',   'Teachers'),
    ('api/subjects',   'Subjects'),
    ('api/students',   'Students'),
    ('api/grades',     'Grades'),
    ('api/attendance', 'Attendance'),
]:
    r = requests.get(f'{BASE_URL}/{endpoint}')
    if r.status_code == 200:
        print(f"   ✅ {nombre:12} → {len(r.json())} registros")
    else:
        print(f"   ❌ {nombre:12} → error {r.status_code}")    