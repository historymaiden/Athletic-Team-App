<script>
$(document).ready(function(){
    var $content1 = $('.content').first().clone();
    $content1.css("display", "block");
    $('div#screen').html($content1);

    $(".tab").live("click", function() {

        var $content = $(this).next('div.content').clone();
        $content.css("display", "block");
        $('div#screen').html($content);
    });
});
</script>