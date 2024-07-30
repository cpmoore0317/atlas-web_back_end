// 11-createEmployeesObject.js

export default function createEmployeeObjects(departmentName, employees) {
  const departmentObject = {
    [departmentName]: employees,
  };

  return departmentObject;
}
