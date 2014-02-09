nunjucks.configure('/static/templates');

$(function () {
    $('button[type="submit"]').click(function (evt) {
        evt.preventDefault();
        evt.stopPropagation();

        $('ul.list-group').append(nunjucks.render('_row.html', {
            'title': $('#name').val(),
            'body': $('#description').val()
        }))
    });
});