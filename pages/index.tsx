import type { NextPage } from "next";
import { Icon } from "@iconify/react";
import MyBanks from "../components/myBanks";
import { useEffect } from "react";

const Home: NextPage = () => {
  useEffect(() => {
    function scroll() {
      window.addEventListener("scroll", function () {
        console.log("scroll");
      });
    }
    scroll();
  }, []);
  return (
    <div className="h-screen w-full bg-dark-800 p-3">
      <header
        className={`sticky w-full flex fixed top-0 justify-between text-gray-500`}
      >
        <div className="font-bold text-3xl">toss</div>
        <div className="flex gap-x-6">
          <button>
            <Icon
              icon="ant-design:message-filled"
              width={28}
              height={28}
              className="items-center flex"
            />
          </button>
          <button>
            <Icon
              icon="ion:notifications"
              width={28}
              height={28}
              className="items-center flex"
            />
          </button>
        </div>
      </header>

      <main>
        <button className="w-full bg-dark-600 items-center flex rounded-lg p-4 justify-between">
          <div className="text-white font-font-bold">존스뱅크</div>
          <Icon icon="ic:round-navigate-next" className="text-white" />
        </button>

        <div className="flex  flex-col w-full gap-4 p-4 bg-dark-600 rounded-lg ">
          <button className="flex justify-between items-center w-full">
            <div className="text-white text-lg font-bold ">자산</div>
            <Icon icon="ic:round-navigate-next" className="text-white " />
          </button>

          <div className="flex flex-col gap-4">
            <MyBanks bankName="토스뱅크" money={2000000}></MyBanks>
            <MyBanks bankName="존스뱅크" money={46587394}></MyBanks>
            <MyBanks bankName="노스뱅크" money={28374}></MyBanks>
            <MyBanks bankName="예스뱅크" money={234082}></MyBanks>
          </div>
        </div>
      </main>
    </div>
  );
};

export default Home;
