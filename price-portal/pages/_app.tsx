import React from "react";
import type { AppProps } from "next/app";

import { AuthCode } from "../context/AuthCode";

function MyApp({ Component, pageProps }: AppProps) {
    return <AuthCode children={<Component {...pageProps} />}></AuthCode>;
}

export default MyApp;
