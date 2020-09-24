endpoint = "http://localhost:8080/topics_data";
tableId = "dataTableBody"

function fetch_topics_data() {
    fetch(endpoint)
    .then(response => response.json())
    .then(
        response => reload_table(response),
        error => alert(error)
    )
}

function reload_table(response) {
    if("topics_data" in response) {
        const topicData = response.topics_data;
        let tableCont = "";
        Object.entries(topicData).forEach(
            entry => tableCont += `<tr><td>${entry[0]}</td><td>${entry[1]}</td><td></td></tr>`
        );
        document.getElementById(tableId).innerHTML = tableCont;
    }
}