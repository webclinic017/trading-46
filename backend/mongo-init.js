db.createUser(
    {
        user: "oscar",
        pwd: "12345678",
        roles: [
            {
                role: "readWrite",
                db: "backtest"
            }
        ]
    }
);