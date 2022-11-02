 /* Optional Javascript to close the radio button version by clicking it again */
 var myRadios = document.getElementsByName('tabs2');
 var setCheck;
 var x = 0;
 for(x = 0; x < myRadios.length; x++){
     myRadios[x].onclick = function(){
         if(setCheck != this){
               setCheck = this;
         }else{
             this.checked = false;
             setCheck = null;
     }
     };
 }

 $(document).ready(function(){
     $.getJSON("/faq-review/show_json_faq/", function(data){
       var count = 0;
         $.each(data, function(index, value){
             console.log(value)
             console.log(count)
             $("#faq-element").append(
               `<div class="tab w-full overflow-hidden border-t">
                 <input class="absolute opacity-0" id="tab-single-${count}" type="radio" name="tabs2">
                   <label class="block p-5 leading-normal cursor-pointer" for="tab-single-${count}">${value.fields.question}</label>
                   <div class="tab-content overflow-hidden border-l-2 bg-gray-100 border-indigo-500 leading-normal">
                     <p class="p-5">${value.fields.answer}</p>
                   </div>
               </div>`
             )
             count++;
         })
     })
 })