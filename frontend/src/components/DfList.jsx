import { fakes } from '../constants';
import styles, { layout } from '../style';

const FakeList = ({img, title, content, index, buttonTexts}) => (
    <div className={`flex flex-row p-6 rounded-[20px] ${index !== fakes.length -1 ? "mb-6" : "mb-0"} fake-list`}>
      <div className={`rounded-full ${styles.flexCenter} bg-dimBlue`}>
        <img src={img} alt="deepfake" className="object-contain" style={{ width: '125px', height: '250px' }} />
      </div>
      <div className="flex flex-row ml-3">
        <div className="flex-1 flex flex-col" style={{maxWidth: '470px'}}>
          <h4 className="font-poppins font-semibold text-white text-[18px] leading-[23px] mb-1">
            {title}
          </h4>
          <p className="font-poppins font-normal text-dimWhite text-[16px] leading-[24px] mb-1">
            {content}
          </p>
        </div>
        <div className="flex flex-col ml-3">
        <button className="bg-white text-black px-[8px] py-2 rounded font-poppins mb-2 hover:bg-gray-200 active:bg-gray-300">
         <strong>Respond to Instagram DM:</strong> {buttonTexts[0]}
        </button>
        <button className="bg-white text-black px-[8px] py-2 rounded font-poppins mb-2 hover:bg-gray-200 active:bg-gray-300">
         <strong>Report Instagram DM:</strong> {buttonTexts[1]}
        </button>   
        <button className="bg-white text-black px-[8px] py-2 rounded font-poppins mb-2 hover:bg-gray-200 active:bg-gray-300">
         <strong>Post about Instagram DM:</strong> {buttonTexts[2]}
        </button>

        </div>
      </div>
    </div>
  );
  
  

  const DfList = () => {
    return (
      <section>
        <div className={`p-6 ${layout.sectionImg} flex flex-col justify-start`}>
          {fakes.map((fake, index) => (
            <FakeList key={fake.id} {...fake} index={index}/>
          ))}
        </div>
      </section>
    )
  }
  

export default DfList
