// JS pour le bouton personnalisé d'upload d'image sur la page de création de ticket

document.addEventListener('DOMContentLoaded', function() {
    const fileBtn = document.querySelector('.custom-file-btn');
    const fileInput = document.getElementById('id_image');
    if (fileBtn && fileInput) {
        fileBtn.addEventListener('click', function(e) {
            fileInput.click();
        });
    }
});
