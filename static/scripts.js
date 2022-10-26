document.addEventListener("DOMContentLoaded", () => {
    let todaydate = document.getElementById("issuedate");
    let n =  new Date();
    let y = n.getFullYear();
    let m = n.getMonth() + 1;
    let d = n.getDate();
    if(m < 10)
    m = '0' + m.toString();
    else if(d < 10)
    d = '0' + d.toString();

    let maxDate = y + '-' + m + '-' + d
    if (todaydate) {
        todaydate.setAttribute("max",maxDate);
    }

    setTimeout(fade_out, 10000);

});

function fade_out() {
    $(".message").fadeOut().empty();
}

function addpercentrow() {
    var total_percent = 0;
    var table = document.getElementById("percent-table");
    var rowCount = table.rows.length;
    for (var i = 0; i < table.rows.length; i++) {
        percent = table.rows[i].cells[0].firstChild.value;
        if (percent) {
            total_percent = total_percent + parseInt(percent);
        }
    }
    if (total_percent < 100) {
        for (var i = 0; i < table.rows.length; i++) {
            percent = table.rows[i].cells[0].firstChild.value;
            if (percent) {
                if (i == table.rows.length-1) {
                    var row = table.insertRow(rowCount);
                    var cell1 = row.insertCell(0);
                    var cell2 = row.insertCell(1);
                    var cell3 = row.insertCell(2);
                    var newrow = rowCount + 1;
                    cell1.innerHTML = '<td><input name="percent[]" id="percent'+ newrow +'" type="number" onchange="addpercentrow(this)"></td>'
                    cell2.innerHTML = '<td>% upon</td>'
                    cell3.innerHTML = '<td><input name="remark[]" id="remark'+ newrow +'" type="text"></td>'
                    break
                }
            }
        }
    } else if (total_percent == 100) {
        for (var i = 0; i < table.rows.length; i++) {
            percent = table.rows[i].cells[0].firstChild.value;
            if (!percent) {
                table.deleteRow(i);
            }
        }
    }
}