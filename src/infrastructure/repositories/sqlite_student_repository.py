from src.core.domain import Student
from src.core.ports.istudent_repository import IStudentRepository
import sqlite3

class SqliteStudentRepository(IStudentRepository):

    def __init__(self, config_str):
        self.connection = sqlite3.connect(config_str)

    def save(self, student: Student) -> str:
        # Guardar en la base de datos
        cursor = self.connection.cursor()
        try:
            cursor.execute(
                "INSERT INTO users (user_id, first_name, last_name, email) VALUES (?, ?, ?, ?)",
                (student.telegram_id, student.first_name, student.last_name, student.email)
            )
            self.connection.commit()
        except sqlite3.IntegrityError:
            answer_message = "❌ Error: Ya estás registrado."
        finally:
            self.connection.close()

        answer_message = (
            f"✅ *Registro completado* ✅\n\n"
            f"• Nombre: {student.first_name} {student.last_name}\n"
            f"• Email: {student.email}\n"
            f"• Curso: {student.course_name}"
        )
        return answer_message

    def find_by_id(self, student_id: str) -> Student | None:
        cursor = self.connection.cursor()
        try:
            cursor.execute(
            "SELECT id_student, first_name, last_name, email FROM students WHERE telegram_id = ?",
            (student_id,)
            )
            row = cursor.fetchone()
            if row:
                return Student(
                    telegram_id=row[0],
                    first_name=row[1],
                    last_name=row[2],
                    email=row[3]
                )
        except sqlite3.Error as e:
            print(f"Database error: {e}")
        finally:
            cursor.close()
        return None