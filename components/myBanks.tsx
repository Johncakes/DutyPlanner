export default function MyBanks(props: { bankName: string; money: number }) {
  return (
    <>
      <div
        className="flex w-full justify-between gap-5 items-center "
        onClick={() => {
          console.log("body");
        }}
      >
        <div className="flex gap-4 items-center">
          <div className="rounded-full w-12 h-12 flex justify-center items-center bg-white">
            I
          </div>
          <div className="flex flex-col  items-start">
            <div className="text-gray-500 ">{props.bankName}통장</div>
            <div className="font-semibold text-xl text-white">
              {props.money.toLocaleString()} 원
            </div>
          </div>
        </div>
        <button
          className="px-3 py-2 bg-dark-200 text-gray-300 rounded-md text-sm "
          onClick={(e) => {
            e.stopPropagation();
            console.log("Button");
          }}
        >
          송금
        </button>
      </div>
    </>
  );
}
