// variable that keeps all the filter information


var send_data = {}

$(document).ready(function () {
    // reset all parameters on page load
    resetFilters();

    getAPIData();
    getAIDSStatus();
    getMalariaStatus();
    getEbolaStatus();
    getCOVID19Status();

    $('#AIDS_status').on('change', function () {
        // update the selected AIDS_status
        if(this.value == "all")
            send_data['AIDS_status'] = "";

        else
            send_data['AIDS_status'] = this.value;
            
        getAPIData();
    });

    $('#malaria_status').on('change', function () {
        // update the selected malaria_status
        if(this.value == "all")
            send_data['malaria_status'] = "";

        else
            send_data['malaria_status'] = this.value;
            
        getAPIData();
    });

    $('#ebola_status').on('change', function () {
        // update the selected ebola_status
        if(this.value == "all")
            send_data['ebola_status'] = "";

        else
            send_data['ebola_status'] = this.value;
            
        getAPIData();
    });

    $('#COVID19_status').on('change', function () {
        // update the selected COVID19_status
        if(this.value == "all")
            send_data['COVID19_status'] = "";

        else
            send_data['COVID19_status'] = this.value;
            
        getAPIData();
    });

    // sort the data according to age
    $('#sort_by').on('change', function () {
        send_data['sort_by'] = this.value;
        getAPIData();
    });

    // display the results after reseting the filters
    $("#display_all").click(function(){
        resetFilters();
        getAPIData();
    })
})

/**
    Function that resets all the filters   
**/
function resetFilters() {
    $("#AIDS_status").val("all");
    $("#malaria_status").val("all");
    $("#ebola_status").val("all");
    $("#COVID19_status").val("all");
    $("#sort_by").val("none");

    //clearing up the select boxes
    getAIDSStatus("all");
    getMalariaStatus("all");
    getEbolaStatus("all");
    getCOVID19Status("all");

    send_data['AIDS_status'] = '';
    send_data['malaria_status'] = '';
    send_data['ebola_status'] = '';
    send_data['COVID19_status'] = '';
    send_data["sort_by"] = '',
    send_data['format'] = 'json';
}

/**.
    Utility function to showcase the api data 
    we got from backend to the table content
**/
function putTableData(result) {
    // creating table row for each result and

    // pushing to the html cntent of table body of listing table

    let row;
    if(result["results"].length > 0){
        $("#no_results").hide();
        $("#list_data").show();
        $("#listing").html("");  
        $.each(result["results"], function (a, b) {
            row = "<tr> <td>" + b.first_name + "</td>" +
                "<td>" + b.last_name + "</td>" +
                "<td>" + b.age + "</td>" +
                "<td>" + b.sex + "</td>" +
                "<td>" + b.blood_type + "</td>" +
                "<td>" + b.genotype + "</td>" +
                "<td>" + b.AIDS_status + "</td>" +
                "<td>" + b.malaria_status + "</td>" +
                "<td>" + b.ebola_status + "</td>" +
                "<td>" + b.COVID19_status + "</td></tr>"
            $("#listing").append(row);   
        });
    }
    else{
        // if no result found for the given filter, then display no result

        $("#no_results h5").html("No results found");
        $("#list_data").hide();
        $("#no_results").show();
    }
    // setting previous and next page url for the given result

    let prev_url = result["previous"];
    let next_url = result["next"];
    // disabling-enabling button depending on existence of next/prev page. 

    if (prev_url === null) {
        $("#previous").addClass("disabled");
        $("#previous").prop('disabled', true);
    } else {
        $("#previous").removeClass("disabled");
        $("#previous").prop('disabled', false);
    }
    if (next_url === null) {
        $("#next").addClass("disabled");
        $("#next").prop('disabled', true);
    } else {
        $("#next").removeClass("disabled");
        $("#next").prop('disabled', false);
    }
    // setting the url

    $("#previous").attr("url", result["previous"]);
    $("#next").attr("url", result["next"]);
    // displaying result count

    $("#result-count span").html(result["count"]);
}

function getAPIData() {
    let url = $('#list_data').attr("url")
    $.ajax({
        method: 'GET',
        url: url,
        data: send_data,
        beforeSend: function(){
            $("#no_results h5").html("Loading data...");
        },
        success: function (result) {
            putTableData(result);
        },
        error: function (response) {
            $("#no_results h5").html("Something went wrong");
            $("#list_data").hide();
        }
    });
}

$("#next").click(function () {
    // load the next page data and 

    // put the result to the table body

    // by making ajax call to next available url

    let url = $(this).attr("url");
    if (!url)
        $(this).prop('all', true);

    $(this).prop('all', false);
    $.ajax({
        method: 'GET',
        url: url,
        success: function (result) {
            putTableData(result);
        },
        error: function(response){
            console.log(response)
        }
    });
})

$("#previous").click(function () {
    // load the previous page data and 

    // put the result to the table body 

    // by making ajax call to previous available url

    let url = $(this).attr("url");
    if (!url)
        $(this).prop('all', true);

    $(this).prop('all', false);
    $.ajax({
        method: 'GET',
        url: url,
        success: function (result) {
            putTableData(result);
        },
        error: function(response){
            console.log(response)
        }
    });
})

function getAIDSStatus(province) {
    // fill the options of AIDS_status by making ajax call
    // obtain the url from the AIDS_status select input attribute
    let url = $("#AIDS_status").attr("url");
    let option = "<option value='all' selected>All Statuses</option>";

    // makes request to get_test_status(request) method in views
    $.ajax({
        method: 'GET',
        url: url,
        data: {},
        success: function (result) {
            $.each(result["test_status"], function (a, b) {
                option += "<option>" + b + "</option>"
            });
            $("#AIDS_status").html(option);
        },
        error: function(response){
            console.log(response)
        }
    });
}

function getMalariaStatus(province) {
    // fill the options of malaria_status by making ajax call
    // obtain the url from the malaria_status select input attribute
    let url = $("#malaria_status").attr("url");
    let option = "<option value='all' selected>All Statuses</option>";

    // makes request to get_test_status(request) method in views
    $.ajax({
        method: 'GET',
        url: url,
        data: {},
        success: function (result) {
            $.each(result["test_status"], function (a, b) {
                option += "<option>" + b + "</option>"
            });
            $("#malaria_status").html(option);
        },
        error: function(response){
            console.log(response)
        }
    });
}

function getEbolaStatus(province) {
    // fill the options of ebola_status by making ajax call
    // obtain the url from the ebola_status select input attribute
    let url = $("#ebola_status").attr("url");
    let option = "<option value='all' selected>All Statuses</option>";

    // makes request to get_test_status(request) method in views
    $.ajax({
        method: 'GET',
        url: url,
        data: {},
        success: function (result) {
            $.each(result["test_status"], function (a, b) {
                option += "<option>" + b + "</option>"
            });
            $("#ebola_status").html(option);
        },
        error: function(response){
            console.log(response)
        }
    });
}

function getCOVID19Status(province) {
    // fill the options of COVID19_status by making ajax call
    // obtain the url from the COVID19_status select input attribute
    let url = $("#COVID19_status").attr("url");
    let option = "<option value='all' selected>All Statuses</option>";

    // makes request to get_test_status(request) method in views
    $.ajax({
        method: 'GET',
        url: url,
        data: {},
        success: function (result) {
            $.each(result["test_status"], function (a, b) {
                option += "<option>" + b + "</option>"
            });
            $("#COVID19_status").html(option);
        },
        error: function(response){
            console.log(response)
        }
    });
}