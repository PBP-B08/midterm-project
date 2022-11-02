$(document).ready(function() {
    $.getJSON("/faq-review/show_json_review/", function(data){
        $.each(data, function(index,value){
          console.log(value)
            $("#review-card").append( 
                `<div class="border-r border-b border-l border-gray-400 lg:border-l-0 lg:border-t lg:border-gray-400 bg-white rounded-b lg:rounded-b-none lg:rounded-r p-4 flex flex-col justify-between leading-normal">
                    <div class="mb-8">
                        <p class="text-sm text-gray-600 flex items-center">
                            <img class="w-10 h-10 rounded-full mr-4" src="/static/media/review.png">
                        User Review
                        </p>
                        <div class="text-gray-900 font-bold text-xl mb-2">${value.fields.title}</div>
                        <p class="text-gray-700 text-base">${value.fields.review}</p>
                    </div>
                    <div class="flex justify-center items-center">
                        <img class="w-10 h-10 rounded-full mr-4" src="/static/media/profile.png">
                        <div class="text-sm">
                        <p class="text-gray-900 leading-none">${value.fields.username}</p>
                        <p class="text-gray-600">${value.fields.date_add}</p>
                        </div>
                    </div>
                    <div class="flex justify-center mt-10 w-fit items-center space-x-3 py-3 px-6 bg-indigo-600 text-white rounded-lg flex align-items-center transition-all duration-400 transform hover:scale-105 cursor-pointer hover:shadow-lg">
                    <button class="text-lg text-md" data-modal-toggle="submit-modal">
                        <a href="/faq-review/delete/${value.pk}/" class="btn btn-primary">Delete task</a>
                    </button>
                    </div>  
                </div>`
            )
        })
    })

    $("#review-form").on("submit",function(e) {
        e.preventDefault() 
        let title = $("#title").val();
        let review = $("#review").val();
        $.ajax({
          method: "POST",
          url: "/faq-review/add/",
          data: $("#review-form").serialize(),
        }).done(function(resp) {
          console.log(resp)
          $("#review-card").append(
                    `<div class="border-r border-b border-l border-gray-400 lg:border-l-0 lg:border-t lg:border-gray-400 bg-white rounded-b lg:rounded-b-none lg:rounded-r p-4 flex flex-col justify-between leading-normal">
                      <div class="mb-8">
                        <p class="text-sm text-gray-600 flex items-center">
                            <img class="w-10 h-10 rounded-full mr-4" src="/static/media/review.png">
                          User Review
                        </p>
                        <div class="text-gray-900 font-bold text-xl mb-2">${resp.title}</div>
                        <p class="text-gray-700 text-base">${resp.review}</p>
                      </div>
                      <div class="flex items-center">
                        <img class="w-10 h-10 rounded-full mr-4" src="/static/media/profile.png">
                        <div class="text-sm">
                          <p class="text-gray-900 leading-none">${resp.username}</p>
                          <p class="text-gray-600">${resp.date}</p>
                          <a href="/faq-review/delete/${resp.pk}/" class="btn btn-primary">Delete task</a>
                        </div>
                      </div>
                    </div>`
        )
    });
    })
})
