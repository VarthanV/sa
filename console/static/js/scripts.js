var sem;
window.onload = () => {
  var selectDeptNode = document.querySelector("#departmentFormControl");
  var selectTeachersNode = document.querySelector("#selectTeachers");
  var selectSemesterNode = document.querySelector("#semesterFormControl");

  var selectSubjectNode = document.querySelector("#selectSubject");
  selectSemesterNode.addEventListener("change", function(event) {
    sem = event.target.value;
  });
  selectDeptNode.addEventListener("change", function(ev) {
    console.log(ev.target.value);
    var url =
      window.location.protocol +
      "//" +
      window.location.hostname +
      ":" +
      window.location.port +
      "/staffs/";
    var request = new XMLHttpRequest();
    request.open("POST", url);
    request.onload = () => {
      if (request.status == 200) {
        var res = JSON.parse(request.responseText);
        var staffs = res.staffs;
        var subjects = res.subjects;
        for (var i = 0; i < staffs.length; i++) {
          var optionNode = document.createElement("option");
          optionNode.value = staffs[i];
          optionNode.innerHTML = staffs[i];
          selectTeachersNode.appendChild(optionNode);
        }
        for (var i = 0; i < subjects.length; i++) {
          var optionNode = document.createElement("option");
          optionNode.value = subjects[i];
          optionNode.innerHTML = subjects[i];
          selectSubjectNode.appendChild(optionNode);
        }
      }
    };
    request.send(JSON.stringify({ dept: ev.target.value, sem: sem }));
  });

  var url =
    window.location.protocol +
    "//" +
    window.location.hostname +
    ":" +
    window.location.port +
    "/departments/";
  var request = new XMLHttpRequest();
  request.open("GET", url);
  request.onload = () => {
    if (request.status == 200) {
      var depts = JSON.parse(request.responseText);
      console.log(depts);
      for (var i = 0; i < depts.length; i++) {
        var optionNode = document.createElement("option");
        optionNode.value = depts[i];
        optionNode.innerHTML = depts[i];
        selectDeptNode.appendChild(optionNode);
      }
    }
  };
  request.send();
};
