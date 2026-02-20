// JS pour la page de réponse à un ticket (création de critique)
// Ici, il n'y a pas de champ image à uploader, donc pas de bouton upload à gérer.
// Si besoin d'interactivité supplémentaire, ajouter ici.

// Exemple : focus sur le champ titre de la critique

document.addEventListener('DOMContentLoaded', function() {
    const headlineInput = document.getElementById('id_headline');
    if (headlineInput) {
        headlineInput.focus();
    }
});
