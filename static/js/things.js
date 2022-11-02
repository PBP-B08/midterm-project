var prov_id = "{{ prov_id }}";
var role = "{{ role }}";

const addFoodCard = function(food) {
    $("#food-card").append(
        `<div id="food-${food.pk}" class="mx-4 my-6 card text-center">
        <div class="card-front" style="background-image:url(${food.fields.image});"><figcaption>${food.fields.name}</figcaption></div>
        <div id="back-${food.pk}" style="background-image:url(${food.fields.image});" class="card-back">
            <div class="backdrop-blur-sm bg-white/30">
            <h2>${food.fields.name}<br><span>${food.fields.description}</span></h2>
            </div>
        </div>
        </div>`
    )
    if (role == 'admin') {
        $(`#back-${food.pk}`).append(
            `<div class="flex relative">
            <div class="my-3 w-fit items-center m-auto space-x-3 bg-indigo-600 px-3 py-1 text-white rounded-md cursor-pointer hover:shadow-lg">
                <button onclick="deleteFood(${food.pk})" type="button">
                Delete
                </button>
            </div>
            </div>`);
    }
}

const addEventCard = function(event) {
    $("#event-card").append(
        `<!-- Column -->
        <div id="event-${event.pk}" style="width:300px;" class="content-center my-4 w-full mx-3 md:w-1/2 md:my-2 lg:my-4 lg:w-1/3 event">
            <!-- Article -->
            <article style="width:300px;" class="mx-0 content-center justify-center overflow-hidden shadow-lg object-cover ease-in-out duration-500 hover:scale-105 card-event">
                <a>
                    <!-- <img alt="${event.fields.name}" class="block h-auto w-full" src="${event.fields.image}"> -->
                    <img alt="Placeholder" class="block w-full img-event" src="${event.fields.image}">
                </a>
                <header id="eventbtn-${event.pk}" class="text-center items-center justify-between bg-white/75 leading-tight p-2 md:p-4">
                    <h1 class="text-lg">
                        ${event.fields.name}
                    </h1>
                    <h1 class="text-grey-darker text-lg">
                    ${event.fields.date}
                    </h1>
                    <p class="text-grey-darker text-md">
                        ${event.fields.description}
                    </p>
                </header>
            </article>
            <!-- END Article -->
        </div>
        <!-- END Column -->`
        );
    if (role == 'admin') {
        $(`#eventbtn-${event.pk}`).append(
                `<div class="flex my-3 w-fit items-center m-auto space-x-3 mx-30 bg-indigo-600 px-3 py-1 text-white rounded-md cursor-pointer hover:shadow-lg">
                    <button onclick="deleteEvent(${event.pk})" type="button">
                    Delete
                    </button>
                </div>`);
}
}

var safeColors = ['#9F2B68', '#DE3163', '#811331', '#FF7F50',
                '#F88379', '#AA336A', '#C9A9A6', '#FF69B4', '#E37383',
                '#FFB6C1', '#FF00FF', '#770737', '#D8BFD8',
                '#DA70D6', '#F8C8DC', '#FAA0A0', '#FFC0CB', '#F89880', 
                '#673147', '#A95C68', '#800080', '#E30B5C', '	#953553', 
                '#F33A6A', '#C21E56'];
var rand = function() {
    return Math.floor(Math.random()*safeColors.length);
};
var randomColor = function() {
    return safeColors[rand()];
};

$("#grand-pic").css("background", randomColor());

const addFood = function() {
    var formData = $("#add-food").serialize();
    if ($("#fprov_id").val() && $("#fname").val() && $("#fdescription").val() && $("#fimage").val()) {
      $.ajax({
            type: "POST",
            url: "/things-to-do/add/food",
            data: formData,
            dataType: "json",
            encode: true,
            }).done(function (data) {
              addFoodCard(data);
              $("#add-food").trigger("reset");
              closeFoodModalBtn.click();
            //   alert("Berhasil menambahkan makanan baru");
            $("#success-food").show();
        })
    }
  }

const addEvent = function() {
    var formData = $("#add-event").serialize();
    if ($("#eprov_id").val() && $("#ename").val() && $("#edescription").val() && $("#eimage").val() && $("#edate").val()) {
        $.ajax({
            type: "POST",
            url: "/things-to-do/add/event",
            data: formData,
            dataType: "json",
            encode: true,
            }).done(function (data) {
                addEventCard(data);
                $("#add-event").trigger("reset");
                closeEventModalBtn.click();
                // alert("Berhasil menambahkan event baru");
                $("#success-event").show();
            })
    }
}

function deleteFood(pk) {
    $.ajax({
        type: "DELETE",
        headers: { "X-CSRFToken": document.getElementsByName("csrfmiddlewaretoken")[0].value },
        url: `/things-to-do/delete/food/${pk}`,
        encode: true,
        }).done(function (data) {
            $(`#food-${pk}`).remove();
            // alert("Berhasil menghapus makanan");
            $("#danger-food").show();
        })
}

function deleteEvent(pk) {
    $.ajax({
        type: "DELETE",
        headers: { "X-CSRFToken": document.getElementsByName("csrfmiddlewaretoken")[0].value },
        url: `/things-to-do/delete/event/${pk}`,
        encode: true,
        }).done(function (data) {
            $(`#event-${pk}`).remove();
            // alert("Berhasil menghapus event");
            $("#danger-event").show();
        })
}

$(".close").click(function() {
    $(this)
      .parent(".alert")
      .fadeOut();
  });
  
