function setValue(v) {
    let old = parseInt(document.getElementById("pval").value)

    console.log(old, v)
    let SPEED = 40;
    // Retrieve the percentage value
    for (let i = old; i <= old + v; i++) {
        setTimeout(function() {
            document.getElementById("value1").innerHTML = i + "%";
            document.getElementById("bar").style.width = i + "%";
        }, SPEED * i);
    }
    document.getElementById("pval").value = old + v;
}

window.addEventListener('load', () => {
    setValue(0);
})