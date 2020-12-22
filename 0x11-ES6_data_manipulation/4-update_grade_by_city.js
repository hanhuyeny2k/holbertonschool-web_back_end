export default function updateStudentGradeByCity(students, city, newGrades) {
  return students
    .filter((student) => student.city === city)
    .map((student) => {
      const grade = newGrades.find((grade) => grade.studentId === student.id);
      return {
        grade: grade ? grade.grade : 'N/A',
        ...student,
      };
    });
}
