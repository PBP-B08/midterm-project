var prov_id = "{{ prov_id }}";
// get jsevent data
$.getJSON( `/things-to-do/json/food/${prov_id}/`, function( data ) {
    data.forEach(food => {
        addFoodCard(food);
    });
});
// get json event data
$.getJSON( `/things-to-do/json/event/${prov_id}/`, function( data ) {
    data.forEach(event => {
        addEventCard(event);
    });
});

const addFoodCard = function(food) {
$("#food-card").append(
    `<!-- Column -->
    <div class="my-4 px-1 w-full md:w-1/2 md:my-1 lg:my-4 lg:px-4 lg:w-1/3">
        <!-- Article -->
        <article class="overflow-hidden rounded-lg shadow-lg object-cover ease-in-out duration-500 hover:scale-105">
            <a href="">
                <!-- <img alt="${food.fields.name}" class="block h-auto w-full" src="${food.fields.image}"> -->
                <img alt="Placeholder" class="block h-auto w-full" src="${food.fields.image}">
            </a>
            <header class="flex items-center justify-between bg-white/75 leading-tight p-2 md:p-4">
                <h1 class="text-lg">
                    ${food.fields.name}
                </h1>
            </header>
        </article>
        <!-- END Article -->
    </div>
    <!-- END Column -->`
    );
}

const addEventCard = function(event) {
$("#event-card").append(
    `<!-- Column -->
    <div class="my-4 px-1 w-full md:w-1/2 md:my-1 lg:my-4 lg:px-4 lg:w-1/3">
        <!-- Article -->
        <article class="overflow-hidden rounded-lg shadow-lg object-cover ease-in-out duration-500 hover:scale-105">
            <a href="">
                <!-- <img alt="${event.fields.name}" class="block h-auto w-full" src="${event.fields.image}"> -->
                <img alt="Placeholder" class="block h-auto w-full" src="${event.fields.image}">
            </a>
            <header class="flex items-center justify-between bg-white/75 leading-tight p-2 md:p-4">
                <h1 class="text-lg">
                    ${event.fields.name}
                </h1>
                <p class="text-grey-darker text-sm">
                    ${event.fields.date}
                </p>
            </header>
        </article>
        <!-- END Article -->
    </div>
    <!-- END Column -->`
    );
}


// Grabs all the Elements by their IDs which we had given them
let foodModal = document.getElementById("modalfood");
let openFoodModalBtn = document.getElementById("modalfood-open");
let closeFoodModalBtn = document.getElementById("modalfood-close");

let eventModal = document.getElementById("modalevent");
let openEventModalBtn = document.getElementById("modalevent-open");
let closeEventModalBtn = document.getElementById("modalevent-close");

// We want the modal to open when the Open button is clicked
openFoodModalBtn.onclick = function() {
    $("#modalfood").fadeIn();
}
// We want the modal to close when the Close button is clicked
closeFoodModalBtn.onclick = function() {
    $("#modalfood").fadeOut();
}

// The modal will close when the user clicks anywhere outside the modal
window.onclick = function(event) {
    if (event.target == foodModal) {
        $("#modalfood").fadeOut();
    }
}

// We want the modal to open when the Open button is clicked
openEventModalBtn.onclick = function() {
    $("#modalevent").fadeIn();
}
// We want the modal to close when the Close button is clicked
closeEventModalBtn.onclick = function() {
    $("#modalevent").fadeOut();
}

// The modal will close when the user clicks anywhere outside the modal
window.onclick = function(event) {
    if (event.target == eventModal) {
        $("#modalevent").fadeOut();
    }
}

const addFood = function() {
var formData = $("#add-food").serialize();
$.ajax({
    type: "POST",
    url: "/things-to-do/add/food",
    data: formData,
    dataType: "json",
    encode: true,
    }).done(function (data) {
    addFoodCard(data);
    $("#add-food").trigger("reset");
    $("#modalfood").click();
    })
}

const addEvent = function() {
var formData = $("#add-event").serialize();
$.ajax({
    type: "POST",
    url: "/things-to-do/add/event",
    data: formData,
    dataType: "json",
    encode: true,
    }).done(function (data) {
    addEventCard(data);
    $("#add-event").trigger("reset");
    $("#modalevent").click();
    })
}