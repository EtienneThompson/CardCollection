import React, { FunctionComponent, useContext } from "react";
import { useRouter } from "next/router";
import crypto from "crypto";
import { TokenContext, authSetter } from "../context/AuthCode";
import PriceApi from "../api/PriceApi";
import style from "./PageHeader.module.scss";

import Toolbar from "./base/Toolbar";
import Button from "./base/Button";

interface PageHeaderProps {}

const PageHeader: FunctionComponent<PageHeaderProps> = (
    props: PageHeaderProps
) => {
    const { authCode } = useContext(TokenContext);
    const setAuthCode = authSetter();
    const router = useRouter();

    const login = () => {
        function base64URLEncode(str) {
            return str
                .toString("base64")
                .replace(/\+/g, "-")
                .replace(/\//g, "_")
                .replace(/=/g, "");
        }

        function sha256(buffer) {
            return crypto.createHash("sha256").update(buffer).digest();
        }

        var verifier = base64URLEncode(crypto.randomBytes(32));
        var challenge = base64URLEncode(sha256(verifier));
        window.open(
            `https://login.microsoftonline.com/common/oauth2/v2.0/authorize?client_id=8c2d2c18-eb35-4c80-ad3f-00824c81dab3&response_type=code&redirect_uri=${encodeURIComponent(
                "http://localhost:3000/verify/login"
            )}&response_mode=query&scope=openid%20profile&state=12345&code_challenge=${challenge}`,
            "_self"
        );
    };

    const logout = () => {
        setAuthCode("");
    };

    const navToCollection = () => {
        router.push(`/collection/selection?authCode=${authCode}`);
    };

    return (
        <>
            <Toolbar>
                <div className={style.leftText}>
                    Card Collection Price Portal
                </div>
                {authCode && (
                    <Button align={"left"} onClick={navToCollection}>
                        Collection
                    </Button>
                )}
                {}
                {authCode ? (
                    <Button align={"right"} onClick={logout}>
                        Logout
                    </Button>
                ) : (
                    <Button align={"right"} onClick={login}>
                        Login
                    </Button>
                )}
            </Toolbar>
        </>
    );
};

export default PageHeader;
