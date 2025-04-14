from src.core.domain import StudentDomain
from src.core.ports.istudent_repository import IStudentRepository
import sqlite3

class SqliteStudentRepository(IStudentRepository):

    def __init__(self, config_str):
        self.connection = sqlite3.connect(config_str)

    async def save(self, student: StudentDomain) -> str:
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

    async def find_by_id(self, student_id: str) -> StudentDomain | None:
        cursor = self.connection.cursor()
        try:
            cursor.execute(
                "SELECT id_student, first_name, last_name, email FROM students WHERE telegram_id = ?",
                (student_id,)
            )
            row = cursor.fetchone()
            if row:
                return StudentDomain(
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

    async def find_all(self) -> list[StudentDomain]:
        cursor = self.connection.cursor()
        students = []
        try:
            cursor.execute("SELECT telegram_id, first_name, last_name, email FROM students")
            rows = cursor.fetchall()
            for row in rows:
                students.append(
                    StudentDomain(
                        telegram_id=row[0],
                        first_name=row[1],
                        last_name=row[2],
                        email=row[3]
                    )
                )
        except sqlite3.Error as e:
            print(f"Database error: {e}")
        finally:
            cursor.close()
        return students

    async def delete(self, student_id: str) -> None:
        cursor = self.connection.cursor()
        try:
            cursor.execute("DELETE FROM students WHERE telegram_id = ?", (student_id,))
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Database error: {e}")
        finally:
            cursor.close()