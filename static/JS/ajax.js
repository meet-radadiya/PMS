function dropdown() {

            var product_category_id = document.getElementById("productCategoryDropdown");

            var product_sub_category_id = document.getElementById("productSubCategoryDropdown");

            product_sub_category_id.innerHTML = '';

            var request = new XMLHttpRequest();
            request.onreadystatechange = function () {
                if (request.readyState === 4) {

                    var json_array = JSON.parse(request.responseText);

                    for (var i = 0; i < json_array.length; i++) {
                        var opt = document.createElement('option');
                        // noinspection Annotator
                        opt.value = json_array[i].sub_category_id;
                        // noinspection Annotator
                        opt.text = json_array[i].sub_category_name;
                        product_sub_category_id.add(opt);
                    }
                }
            };
            request.open('GET', "/product/load_product_sub_category?category_id=" + product_category_id.value + "", true);
            request.send();
        }