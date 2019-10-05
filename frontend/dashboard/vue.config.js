const cfg = require("../../services.json");

module.exports = {
    devServer: {
        host: cfg["dashboard-front-end-dev"].host,
        port: cfg["dashboard-front-end-dev"].port,
    },
};