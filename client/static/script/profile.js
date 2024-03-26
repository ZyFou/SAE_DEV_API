
var pfp_url_storage = document.getElementById('pfp_url')
var banner_url_storage = document.getElementById('banner_url')


function openPFPdiv() {
    const new_pfp_div = document.getElementById("new_pfp_div")
    new_pfp_div.style.display = "block"
}

function openBANNERdiv() {
    const new_banner_div = document.getElementById("new_banner_div")
    new_banner_div.style.display = "block"
}


function addNewPFP() {
    var profile_picture = document.getElementById('profile_picture')
    const newPfpUrl = document.getElementById("new_pfp").value
    pfp_url_storage.value = newPfpUrl
    profile_picture.src = pfp_url_storage.value

}

function addNewBANNER() {
    var banner_picture = document.getElementById('banner_picture')
    const newBannerUrl = document.getElementById("new_banner").value
    banner_url_storage.value = newBannerUrl
    banner_picture.src = banner_url_storage.value
}


