
function onPageLoad() {
    console.log( "document loaded" );
    var url = "http://127.0.0.1:5001/get_location"; // Use this if you are NOT using nginx which is first 7 tutorials
    
    // Making an AJAX GET request to the backend to get location data
    $.get(url, function(data, status) {
        console.log("got response for get_location_names request");

        if (data && data.location) {
            var locations = data.location;
            var uiLocations = document.getElementById("uiLocations");

            $('#uiLocations').empty();
                            
            // Loop through each location and create a new option element, then append it to the dropdown
            for(var i in locations) {
                var opt = new Option(locations[i]);
                uiLocations.append(opt);
            }
        }
    });
  }
  

function onClickedEstimatePrice() {
    console.log("Estimate price button clicked");

    var sqft = document.getElementById("uiSqft");
    var bhk = getBHKValue();
    var bathrooms = getBathValue();
    var location = document.getElementById("uiLocations");
    var estimatedPrice = document.getElementById("uiEstimatedPrice");

    var url = "http://127.0.0.1:5001/predict_prices";

    // Making an AJAX POST request to the backend to get the estimated price
    $.post(url, {
        total_sqft: parseFloat(sqft.value),
        bhk: bhk,
        bath: bathrooms,
        location: location.value
    },function(data, status) { //handles the response from the backend
        console.log(data.estimated_price);
        estimatedPrice.innerHTML = "<h2>Rs. " + data.estimated_price.toString() + " Lakh</h2>";
        console.log(status);
    });
} 

function getBathValue() {
    var uiBathrooms = document.getElementsByName("uiBathrooms");
    for(var i in uiBathrooms) {
        if(uiBathrooms[i].checked) {
            return parseInt(i)+1;
        }
    }
    return -1; // Invalid Value
}

function getBHKValue() {
    var uiBHK = document.getElementsByName("uiBHK");
    for(var i in uiBHK) {
        if(uiBHK[i].checked) {
            return parseInt(i)+1;
        }
    }
    return -1; // Invalid Value
}

window.onload = onPageLoad;