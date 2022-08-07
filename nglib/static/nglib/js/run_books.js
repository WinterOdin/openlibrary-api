function runBooks(url_data) {

	function convertToCSV(arr) {
		const array = [Object.keys(arr[0])].concat(arr);
		return array.map(it => {
			return Object.values(it).toString().replace(/[\r\n]+/g, "");
		}).join('\n')
	}

	$("#clear-form").on("click", function() {
		$('#id_name').val('');
		$('#id_surname').val('');
	});

	$("#book-form").submit(function(e) {
		e.preventDefault();
		var serializedData = $(this).serialize();

		$.ajax({
			type: 'POST',
			url: url_data,
			headers: {
				"X-Requested-With": "XMLHttpRequest",
			},
			data: serializedData,
			success: function(response) {
				var tableData = response['book_data'];
				var author_data = response['author_data']['docs'][0];

				$("#author-name").text(author_data['name']);
				$("#author-birth").text(author_data['birth_date']);
				$("#author-top").text(author_data['top_work']);

				build(tableData)

				$('#download_csv').show();
				$('#download_csv').on("click", function() {
					var data = convertToCSV(response['book_data']);
					var uri = 'Data:text/csv;charset=utf-8,' + escape(data);
					var link = document.createElement("a");
					link.href = uri;
					link.style = "visibility:hidden";
					link.download = 'data.csv';
					document.body.appendChild(link);
					link.click();
					document.body.removeChild(link);
				});

				$("#loadDiv").fadeOut('fast');
				setTimeout(function() {
					$('#content-container, #pagination-wrapper').fadeIn('fast');
					$('#download_csv, .author-data').fadeIn('slow');
				}, 800);
			},
			error: function(response) {
				console.log("blad")
				$("#loadDiv").hide();
				$('#table-body, #pagination-wrapper').empty();
				$('#myModal').modal('show'); 
			}
		})
	})

	$(document).ajaxStart(function() {
		
		$('#download_csv, .author-data').fadeOut('slow');
		$('#content-container, #pagination-wrapper').fadeOut(100, function() {
			$('#table-body, #pagination-wrapper').empty();
		});
		setTimeout(function(){
			$("#loadDiv").fadeIn('fast');
		}, 800);
	});
}