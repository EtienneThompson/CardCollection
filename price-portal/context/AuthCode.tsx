import React, { FunctionComponent, useState, useMemo, useContext } from "react";

type AuthContext = {
    authCode: string;
    setAuthCode: React.Dispatch<React.SetStateAction<string>>;
};

export const TokenContext = React.createContext({} as AuthContext);

export function AuthCode({ children }) {
    const [authCode, setAuthCode] = useState("");
    const ctx = useMemo(() => ({ authCode, setAuthCode }), [authCode]);

    return (
        <TokenContext.Provider value={ctx}>{children}</TokenContext.Provider>
    );
}

export function authSetter() {
    const ctx = useContext(TokenContext);
    return ctx.setAuthCode;
}
