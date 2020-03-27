var contract;

$('#contracts div button').click(function() {
   contract = $(this).attr('data-id'); 
});

$('#contdel').on('show.bs.modal', function (e) {
    $(this).find('.contId').text(contract);
});