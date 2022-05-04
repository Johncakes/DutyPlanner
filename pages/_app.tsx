import type { AppProps } from "next/app";
import Head from "next/head";
import "windi.css";

function MyApp({ Component, pageProps }: AppProps) {
  return (
    <>
      <Head>
        <title>존스뱅크</title>
      </Head>
      <Component {...pageProps} />
    </>
  );
}

export default MyApp;
