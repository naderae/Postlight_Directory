 $(document).ready(function () {

  /* Functions */
  // this function will be used to make the ajax requast to load the form on the page
  // it is seperate from the function to submit the form
  var loadForm = function () {
    // 'this' refers to the add employee button
    var btn = $(this);
    $.ajax({
      // grab the url from the data-url attribute on the button
      url: btn.attr("data-url"),
      // a get request because we loading data onto the page
      type: 'get',
      dataType: 'json',
      // before sending the ajax request to the view(controller), we want to show the modal
      beforeSend: function () {
        $("#modal-employee").modal("show");
      },
      // after recieving the data, rende the form in partial_employee_create
      success: function (data) {
        $("#modal-employee .modal-content").html(data.html_form);
      }
    });
  };

  var saveForm = function () {
    // this (obviously) refers to the form
    var form = $(this);
    $.ajax({
      // as before we grab the url from the action attibute of the form
      url: form.attr("action"),
      // we serialize the data we recieve from the form, so that its in a format we can use, and sending it to our backend
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',
      success: function (data) {
        // with the data, we perform some DOM manipulation
        if (data.form_is_valid) {
          // replace the table body with the updated list
          $("#employee-table tbody").html(data.html_employee_list);
          // hide the modal after sucess
          $("#modal-employee").modal("hide");
        }
        else {
          // if it's we dont recieve a successful reponse, we re-render the form
          $("#modal-employee .modal-content").html(data.html_form);
        }
      }
    });
    // we dont want to the form to create an HTTP request, we so we return false to cancel this default behavior
    return false;
  };


  // Create employee

  // we are listening for a click on the add employee button to load the form onto tha page
  $(".js-create-employee").click(loadForm);
  // when the use clicks the submit button (or Enter key), we run the saveForm method
  // we register the click event to an element that always exists on the page, the modal ,to avoid problems with targeting elements not yet placed in the dom.
  // after all ,due to event propogation will allow us
  $("#modal-employee").on("submit", ".js-employee-create-form", saveForm);

  // Update employee: DONE PRETTY MUCH THE SAME WAY AS CREATE EMPLOYEE
  $("#employee-table").on("click", ".js-update-employee", loadForm);
  $("#modal-employee").on("submit", ".js-employee-update-form", saveForm);

  // delete employees
  $("#employee-table").on("click", ".js-delete-employee", loadForm);
  $("#modal-employee").on("submit", ".js-employee-delete-form", saveForm);


  // search for employees
  // doesnt work with pagination

  // $("#searchBar").on("keyup", function(){
  //   var term = $(this).val().toLowerCase();
  //   $("#table-body tr").filter(function(){
  //     $(this).toggle($(this).text().toLowerCase().indexOf(term) > -1)
  //   });
  // });


  // sort table
  // upon clicking on a table header
  $('th').click(function(){

    // grab the table
    var table = $(this).parents('table').eq(0)
    // grab the rows: from the table, convert it to an array of table rows, and sort it accoridng to alphabetical order, or numeric order
    var rows = table.find('tr:gt(0)').toArray().sort(comparer($(this).index()))

    this.asc = !this.asc
    // if the headers arent in ascending order, reverse the order of the rows to account for clicking multiple times
    if (!this.asc){rows = rows.reverse()}
    // go through all the rows, and add the rows to the table in the order defined above
    for (var i = 0; i < rows.length; i++){table.append(rows[i])}
})

// this function determines the ordering of the elements
// tis function grabs two cell values, if they are numbers, we get the differece(to see which comes before), and if not, we compare the strings to see which comes before in order: a negative means that comes before valB, vice versa
function comparer(index) {
    return function(a, b) {
        var valA = getCellValue(a, index), valB = getCellValue(b, index)
        return $.isNumeric(valA) && $.isNumeric(valB) ? valA - valB : valA.toString().localeCompare(valB)
    }
}
// this function first grabs all the cells that exist on the row, and constructs 1 new element with index = 'index', then grabs the its value
function getCellValue(row, index){ return $(row).children('td').eq(index).text() }

});
