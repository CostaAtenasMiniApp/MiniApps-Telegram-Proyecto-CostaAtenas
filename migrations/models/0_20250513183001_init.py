from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "academiccoordinator" (
    "coordinator_id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "name" VARCHAR(255) NOT NULL,
    "email" VARCHAR(255) NOT NULL
);
CREATE TABLE IF NOT EXISTS "course" (
    "course_id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "name" VARCHAR(255) NOT NULL,
    "description" TEXT NOT NULL,
    "start_date" DATE NOT NULL,
    "duration" INT NOT NULL,
    "status" VARCHAR(50) NOT NULL,
    "coordinator_id" INT NOT NULL REFERENCES "academiccoordinator" ("coordinator_id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "discovery_methods" (
    "method_id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "name" VARCHAR(100) NOT NULL UNIQUE /* Método por el cual el estudiante conoció el curso */,
    "category" VARCHAR(50) NOT NULL /* Categoría del método (social_media, referral, etc.) */,
    "icon" VARCHAR(50) /* Icono de FontAwesome o similar para representación visual */,
    "is_active" INT NOT NULL DEFAULT 1
);
CREATE TABLE IF NOT EXISTS "module" (
    "module_id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "name" VARCHAR(255) NOT NULL,
    "description" TEXT NOT NULL,
    "course_id_id" INT NOT NULL REFERENCES "course" ("course_id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "evaluation" (
    "evaluation_id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "score" INT NOT NULL,
    "feedback" TEXT NOT NULL,
    "course_id_id" INT NOT NULL REFERENCES "course" ("course_id") ON DELETE CASCADE,
    "module_id_id" INT NOT NULL REFERENCES "module" ("module_id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "lesson" (
    "lesson_id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "title" VARCHAR(255) NOT NULL,
    "content" TEXT NOT NULL,
    "module_id_id" INT NOT NULL REFERENCES "module" ("module_id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "professor" (
    "professor_id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "name" VARCHAR(255) NOT NULL,
    "email" VARCHAR(255) NOT NULL
);
CREATE TABLE IF NOT EXISTS "scholarship" (
    "code" VARCHAR(50) NOT NULL PRIMARY KEY,
    "discount_percentage" INT NOT NULL,
    "valid_until" DATE,
    "max_uses" INT,
    "current_uses" INT NOT NULL DEFAULT 0,
    "created_by_id" INT REFERENCES "professor" ("professor_id") ON DELETE CASCADE /* Profesor que creó la beca */
);
CREATE TABLE IF NOT EXISTS "students" (
    "student_id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "email" VARCHAR(255) NOT NULL UNIQUE /* Correo electrónico */,
    "first_name" VARCHAR(255) NOT NULL /* Nombres */,
    "last_name" VARCHAR(255) NOT NULL /* Apellidos */,
    "national_id" VARCHAR(50) UNIQUE /* Número documento nacional de identidad */,
    "phone" VARCHAR(20) /* Número de teléfono (vinculado a Telegram) */,
    "country" VARCHAR(100) /* País */,
    "city" VARCHAR(100) /* Ciudad */,
    "is_proplayas_member" INT NOT NULL DEFAULT 0 /* Miembro de la Red Proplayas? */,
    "proplayas_node" VARCHAR(255) /* Nodo Proplayas (solo si es miembro Proplayas) */,
    "belongs_to_hotel" INT NOT NULL DEFAULT 0 /* Pertenece a algún hotel? */,
    "hotel_name" VARCHAR(255) /* Nombre del hotel */,
    "age" INT /* Edad */,
    "other_discovery_info" TEXT /* Detalles adicionales cuando se selecciona 'Otro' */,
    "referral_info" TEXT /* Referido por un amigo\/colega o información adicional */,
    "education_level" VARCHAR(100) /* Nivel educacional */,
    "study_area" VARCHAR(255) /* Área de estudios */,
    "work_area" VARCHAR(255) /* Área laboral o de interés */,
    "course_motivation" TEXT /* Por qué quieres realizar el curso móvil? */,
    "wants_certification_info" INT NOT NULL DEFAULT 0 /* ¿Recibir información sobre certificación y gestión de playas? */,
    "registration_date" TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "scholarship_id" VARCHAR(50) REFERENCES "scholarship" ("code") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "enrollment" (
    "enrollment_id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "enrollment_date" TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "course_id_id" INT NOT NULL REFERENCES "course" ("course_id") ON DELETE CASCADE,
    "student_id_id" INT NOT NULL REFERENCES "students" ("student_id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "student_discovery_methods" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "details" TEXT /* Detalles específicos (ej. nombre de quien refirió) */,
    "created_at" TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "method_id" INT NOT NULL REFERENCES "discovery_methods" ("method_id") ON DELETE CASCADE,
    "student_id" INT NOT NULL REFERENCES "students" ("student_id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSON NOT NULL
);
CREATE TABLE IF NOT EXISTS "course_professor" (
    "course_id" INT NOT NULL REFERENCES "course" ("course_id") ON DELETE CASCADE,
    "professor_id" INT NOT NULL REFERENCES "professor" ("professor_id") ON DELETE CASCADE
);
CREATE UNIQUE INDEX IF NOT EXISTS "uidx_course_prof_course__d019dd" ON "course_professor" ("course_id", "professor_id");
CREATE TABLE IF NOT EXISTS "scholarship_course" (
    "scholarship_id" VARCHAR(50) NOT NULL REFERENCES "scholarship" ("code") ON DELETE CASCADE,
    "course_id" INT NOT NULL REFERENCES "course" ("course_id") ON DELETE CASCADE
) /* Cursos aplicables para esta beca */;
CREATE UNIQUE INDEX IF NOT EXISTS "uidx_scholarship_scholar_5cabca" ON "scholarship_course" ("scholarship_id", "course_id");
CREATE TABLE IF NOT EXISTS "students_course" (
    "students_id" INT NOT NULL REFERENCES "students" ("student_id") ON DELETE CASCADE,
    "course_id" INT NOT NULL REFERENCES "course" ("course_id") ON DELETE CASCADE
);
CREATE UNIQUE INDEX IF NOT EXISTS "uidx_students_co_student_cea02e" ON "students_course" ("students_id", "course_id");"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """
