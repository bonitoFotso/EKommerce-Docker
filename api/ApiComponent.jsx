// Importez Axios et éventuellement d'autres dépendances nécessaires
import axios from 'axios';

import config from 'src/config'; // Assurez-vous que config.js est correctement configuré


// Fonction pour effectuer une requête API générique
const ApiComponent = async (path, method, data = null) => {
    try {
        // Récupérez le header depuis le localStorage
        const header = localStorage.getItem('header');

        // Récupérez la base de l'API depuis config.js
        const baseURL = config.apiBaseURL;

        // Construisez l'URL complète en ajoutant le chemin d'API fourni en paramètre
        const url = `${baseURL}/${path}`;

        // Construisez les options de requête en fonction du type de requête et des données
        const requestOptions = {
            method,
            headers: {
                'Content-Type': 'application/json',
                'Authorization': header, // Ajoutez le header récupéré du localStorage
            },
            data: data ? JSON.stringify(data) : null,
        };

        // Effectuez la requête Axios
        const response = await axios(url, requestOptions);

        // Retournez la réponse de la requête
        return response.data;
    } catch (error) {
        // Gérez les erreurs ici
        console.error('Erreur lors de la requête API:', error);
        throw error;
    }
};

export default ApiComponent;

