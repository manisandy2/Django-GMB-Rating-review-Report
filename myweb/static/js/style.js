
var table1 = document.getElementsByClassName('first_reviews');
var table2 = document.getElementsByClassName('second_reviews');
var table3 = document.getElementsByClassName('third_review');


function addvalue(){
    for (let i = 0; i < table1.length ; i++) {
        // console.log(tableclass[i].innerHTML)
        table3[i].innerHTML = table2[i].innerHTML - table1[i].innerHTML
        // table3[i]
    }
}

window.onload = addvalue()

// var asm = document.getElementById('#asm_id')

// function asm_dup_remove(){
//     asm.onchange(alert(asm))

// };
// // $(".asm_id").each(function() {
// //     $(this).siblings('[value="'+ this.value +'"]').remove();
// //   });

// window.onload = asm_dup_remove()