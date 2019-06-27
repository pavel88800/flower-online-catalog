$(document).ready(function(){


//Транслитерация кириллицы в URL
function urlRusLat(str) {
	str = str.toLowerCase(); // все в нижний регистр
		var cyr2latChars = new Array(
				['а', 'a'], ['б', 'b'], ['в', 'v'], ['г', 'g'],
				['д', 'd'],  ['е', 'e'], ['ё', 'yo'], ['ж', 'zh'], ['з', 'z'],
				['и', 'i'], ['й', 'y'], ['к', 'k'], ['л', 'l'],
				['м', 'm'],  ['н', 'n'], ['о', 'o'], ['п', 'p'],  ['р', 'r'],
				['с', 's'], ['т', 't'], ['у', 'u'], ['ф', 'f'],
				['х', 'h'],  ['ц', 'c'], ['ч', 'ch'],['ш', 'sh'], ['щ', 'shch'],
				['ъ', ''],  ['ы', 'y'], ['ь', ''],  ['э', 'e'], ['ю', 'yu'], ['я', 'ya'],

				['А', 'A'], ['Б', 'B'],  ['В', 'V'], ['Г', 'G'],
				['Д', 'D'], ['Е', 'E'], ['Ё', 'YO'],  ['Ж', 'ZH'], ['З', 'Z'],
				['И', 'I'], ['Й', 'Y'],  ['К', 'K'], ['Л', 'L'],
				['М', 'M'], ['Н', 'N'], ['О', 'O'],  ['П', 'P'],  ['Р', 'R'],
				['С', 'S'], ['Т', 'T'],  ['У', 'U'], ['Ф', 'F'],
				['Х', 'H'], ['Ц', 'C'], ['Ч', 'CH'], ['Ш', 'SH'], ['Щ', 'SHCH'],
				['Ъ', ''],  ['Ы', 'Y'],
				['Ь', ''],
				['Э', 'E'],
				['Ю', 'YU'],
				['Я', 'YA'],

				['a', 'a'], ['b', 'b'], ['c', 'c'], ['d', 'd'], ['e', 'e'],
				['f', 'f'], ['g', 'g'], ['h', 'h'], ['i', 'i'], ['j', 'j'],
				['k', 'k'], ['l', 'l'], ['m', 'm'], ['n', 'n'], ['o', 'o'],
				['p', 'p'], ['q', 'q'], ['r', 'r'], ['s', 's'], ['t', 't'],
				['u', 'u'], ['v', 'v'], ['w', 'w'], ['x', 'x'], ['y', 'y'],
				['z', 'z'],

				['A', 'A'], ['B', 'B'], ['C', 'C'], ['D', 'D'],['E', 'E'],
				['F', 'F'],['G', 'G'],['H', 'H'],['I', 'I'],['J', 'J'],['K', 'K'],
				['L', 'L'], ['M', 'M'], ['N', 'N'], ['O', 'O'],['P', 'P'],
				['Q', 'Q'],['R', 'R'],['S', 'S'],['T', 'T'],['U', 'U'],['V', 'V'],
				['W', 'W'], ['X', 'X'], ['Y', 'Y'], ['Z', 'Z'],

				[' ', '_'],['0', '0'],['1', '1'],['2', '2'],['3', '3'],
				['4', '4'],['5', '5'],['6', '6'],['7', '7'],['8', '8'],['9', '9'],
				['-', '-']

    );

    var newStr = new String();

    for (var i = 0; i < str.length; i++) {

        ch = str.charAt(i);
        var newCh = '';

        for (var j = 0; j < cyr2latChars.length; j++) {
            if (ch == cyr2latChars[j][0]) {
                newCh = cyr2latChars[j][1];

            }
        }
        // Если найдено совпадение, то добавляется соответствие, если нет - пустая строка
        newStr += newCh;

    }
    // Удаляем повторяющие знаки - Именно на них заменяются пробелы.
    // Так же удаляем символы перевода строки, но это наверное уже лишнее
    return newStr.replace(/[_]{2,}/gim, '_').replace(/\n/gim, '');
}
    $('.category-title').change(function(e){
         let value = $(this).val().replace(/^\s*(.*)\s*$/, '$1');
        $('.category-slug').val(urlRusLat(value));
    });
    $('.sub-category-title').change(function(e){
         let value = $(this).val().replace(/^\s*(.*)\s*$/, '$1');
        $('.sub-category-slug').val(urlRusLat(value));
    });

    $(document).on("change",'#category',function(){ //ajax подгрузка подкатегорий для каждой котегории
        if($(this).val() != ''){
            $.ajax({
                type:'post',
                url: $('.get_subcategory').val(),
                data:{id:$(this).val(), csrfmiddlewaretoken:$( "[name='csrfmiddlewaretoken']" ).val()},
                success:function(res){
                $('#sub_category').html('');
                    for(let i in res){
                        $('#sub_category').append('<option value="'+res[i].pk+'">'+res[i].fields.title+'</option>');
                    }
                }
            });
        }else{
            $('#sub_category').html('');
        }
    })

})