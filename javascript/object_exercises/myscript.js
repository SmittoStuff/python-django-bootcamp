var employee = {
  name: "Big Boi",
  job: "Beast",
  age: 24,
  nameLength: function() {
    console.log(this.name.length);
  }
}

var employee = {
  name: "Big Boi",
  job: "Beast",
  age: 24,
  report: function() {
    alert("Name is " + this.name + ", Job is: " + this.job + ", Age is: " + this.age);
  }
}

var employee = {
  name: "Big Boi",
  job: "Beast",
  age: 24,
  lastName: function() {
    console.log(this.name.split(" ")[1]);
  }
}
