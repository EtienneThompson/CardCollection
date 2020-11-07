import React, { FunctionComponent, useEffect } from "react";
import { useRouter } from "next/router";
import { GetServerSideProps } from "next";
import { authSetter } from "../../context/AuthCode";

import PageHeader from "../../components/PageHeader";

export interface LoginProps {
    authCode: string;
}

export const getServerSideProps: GetServerSideProps = async (context) => {
    const authCode = context.query.code ? context.query.code : "";
    return {
        props: {
            authCode,
        },
    };
};

const Login: FunctionComponent<LoginProps> = (props: LoginProps) => {
    const setAuthCode = authSetter();
    const router = useRouter();

    useEffect(() => {
        setAuthCode(props.authCode);
        router.push("/");
    });

    return (
        <>
            <PageHeader />
        </>
    );
};

export default Login;
