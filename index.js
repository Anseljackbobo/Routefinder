function initMap() {
    const directionsService = new google.maps.DirectionsService();
    const directionsRenderer = new google.maps.DirectionsRenderer();
    const map = new google.maps.Map(document.getElementById("map"), {
        zoom: 6,
        center: { lat: 40.753805, lng: -73.262773 },
    });

    directionsRenderer.setMap(map);
    document.getElementById("Firstpath").addEventListener("click", () => {
        calculateAndDisplayRoute1(directionsService, directionsRenderer);
    });
    document.getElementById("Secondpath").addEventListener("click", () => {
        calculateAndDisplayRoute2(directionsService, directionsRenderer);
    });
    document.getElementById("Thirdpath").addEventListener("click", () => {
        calculateAndDisplayRoute3(directionsService, directionsRenderer);
    });
}




function calculateAndDisplayRoute1(directionsService, directionsRenderer) {

    const waypts = [{ location: "40.762499,-73.242091", stopover: true }, { location: "40.757722,-73.222719", stopover: true }, { location: "40.75917,-73.220675", stopover: true }, { location: "40.761438,-73.213124", stopover: true }, { location: "40.757599,-73.212008", stopover: true }, { location: "40.75149,-73.109407", stopover: true }, { location: "40.760255,-73.109651", stopover: true }, { location: "40.760223,-73.101673", stopover: true }, { location: "40.782895,-72.948645", stopover: true }, { location: "40.779748,-72.946334", stopover: true }, { location: "40.78258,-72.941764", stopover: true }, { location: "40.776474,-72.944977", stopover: true }, { location: "40.774638,-72.946096", stopover: true }, { location: "40.757944,-72.934189", stopover: true }, { location: "40.759037,-72.948293", stopover: true }, { location: "40.763906,-72.948829", stopover: true }, { location: "40.762978,-72.950075", stopover: true }, { location: "40.755896,-73.040668", stopover: true }, { location: "40.751992,-73.034939", stopover: true }, { location: "40.746215,-73.040969", stopover: true }, { location: "40.738368,-73.040662", stopover: true }, { location: "40.737672,-73.040034", stopover: true }];


    directionsService
        .route({
            origin: "40.753805,-73.262773",
            destination: "40.748152,-73.022929",
            waypoints: waypts,
            optimizeWaypoints: true,
            travelMode: google.maps.TravelMode.DRIVING,
        })
        .then((response) => {
            directionsRenderer.setDirections(response);

            const route = response.routes[0];
            const summaryPanel = document.getElementById("directions-panel");

            summaryPanel.innerHTML = "";

            // For each route, display summary information.
            for (let i = 0; i < route.legs.length; i++) {
                const routeSegment = i + 1;

                summaryPanel.innerHTML +=
                    "<b>Route Segment: " + routeSegment + "</b><br>";
                summaryPanel.innerHTML += route.legs[i].start_address + " to ";
                summaryPanel.innerHTML += route.legs[i].end_address + "<br>";
                summaryPanel.innerHTML += route.legs[i].distance.text + "<br><br>";
            }
        })
        .catch((e) => window.alert("Directions request failed due to " + status));
}

function calculateAndDisplayRoute2(directionsService, directionsRenderer) {

    const waypts2 = [{ location: "40.758066,-73.030955", stopover: true }, { location: "40.764478,-73.037521", stopover: true }, { location: "40.770902,-73.068619", stopover: true }, { location: "40.77048,-73.090446", stopover: true }, { location: "40.76801,-73.108536", stopover: true }, { location: "40.75956,-73.115518", stopover: true }, { location: "40.756649,-73.128869", stopover: true }, { location: "40.780397,-73.14201", stopover: true }, { location: "40.779191,-73.271201", stopover: true }, { location: "40.792865,-73.247154", stopover: true }, { location: "40.797541,-73.251704", stopover: true }, { location: "40.802537,-73.25931", stopover: true }, { location: "40.759234,-73.482446", stopover: true }, { location: "40.766091,-73.499887", stopover: true }, { location: "40.752649,-73.486563", stopover: true }, { location: "40.751973,-73.486628", stopover: true }, { location: "40.752536,-73.480586", stopover: true }, { location: "40.741314,-73.486012", stopover: true }, { location: "40.737944,-73.483159", stopover: true }, { location: "40.734832,-73.47807", stopover: true }]


    directionsService
        .route({
            origin: "40.748152,-73.022929",
            destination: "40.7308,-73.481184",
            waypoints: waypts2,
            optimizeWaypoints: true,
            travelMode: google.maps.TravelMode.DRIVING,
        })
        .then((response) => {
            directionsRenderer.setDirections(response);

            const route = response.routes[0];
            const summaryPanel = document.getElementById("directions-panel");

            summaryPanel.innerHTML = "";

            // For each route, display summary information.
            for (let i = 0; i < route.legs.length; i++) {
                const routeSegment = i + 1;

                summaryPanel.innerHTML +=
                    "<b>Route Segment: " + routeSegment + "</b><br>";
                summaryPanel.innerHTML += route.legs[i].start_address + " to ";
                summaryPanel.innerHTML += route.legs[i].end_address + "<br>";
                summaryPanel.innerHTML += route.legs[i].distance.text + "<br><br>";
            }
        })
        .catch((e) => window.alert("Directions request failed due to " + status));
}

function calculateAndDisplayRoute3(directionsService, directionsRenderer) {

    const waypts3 = [{ location: "40.726239,-73.271211", stopover: true }, { location: "40.710915,-73.255459", stopover: true }, { location: "40.71269,-73.259093", stopover: true }, { location: "40.717813,-73.26572", stopover: true }, { location: "40.722121,-73.261863", stopover: true }, { location: "40.723044,-73.261396", stopover: true }, { location: "40.728523,-73.264099", stopover: true }, { location: "40.729096,-73.265498", stopover: true }, { location: "40.72976,-73.263308", stopover: true }]

    directionsService
        .route({
            origin: "40.7308,-73.481184",
            destination: "40.753805,-73.262773",
            waypoints: waypts3,
            optimizeWaypoints: true,
            travelMode: google.maps.TravelMode.DRIVING,
        })
        .then((response) => {
            directionsRenderer.setDirections(response);

            const route = response.routes[0];
            const summaryPanel = document.getElementById("directions-panel");

            summaryPanel.innerHTML = "";

            // For each route, display summary information.
            for (let i = 0; i < route.legs.length; i++) {
                const routeSegment = i + 1;

                summaryPanel.innerHTML +=
                    "<b>Route Segment: " + routeSegment + "</b><br>";
                summaryPanel.innerHTML += route.legs[i].start_address + " to ";
                summaryPanel.innerHTML += route.legs[i].end_address + "<br>";
                summaryPanel.innerHTML += route.legs[i].distance.text + "<br><br>";
            }
        })
        .catch((e) => window.alert("Directions request failed due to " + status));
}

// function showall(A, B, C) {

// }