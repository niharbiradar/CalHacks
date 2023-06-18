import styles from '../style';
import { discount, robot } from '../assets';
import GetStarted from './GetStarted'

const Hero = () => (
  <section id="home" className={`flex md:flex-row flex-col ${styles.paddingY}`}>
    <div className={`flex-1 ${styles.flexStart} flex-col xl:px-0 sm:px-16 px-6`}>
      <div className="flex flex-row items-center py-[6px] px-4 bg-discount-gradient rounded-[10px] mb-2">
        <img src={discount} alt="discount" className="w-[32px] h-[32px]"/>
        <p className={`${styles.paragraph} ml-2`}>
          <span className="text-white">20%
          </span> Discount For {" "}
          <span className="text-white">6 Months
          </span> On New Accounts
        </p>
      </div>

      <div className="flex flex-row justify-between items-center w-full">
        <h1 className="flex-1 font-poppins font-semibold ss:text-[72px] text-[52px] text-white ss:leading-[100px] leading-[75px]">
          <span className="text-gradient">Shielding
          </span> <br className="sm:block hidden" />
           You From 
        </h1>
        <div className="ss:flex hidden md:mr-4 mr-0">
          <GetStarted />
        </div>
      </div>
      <h1 className="flex-1 font-poppins font-semibold ss:text-[68px] text-[52px] text-white ss:leading-[100px] leading-[75px] -mb-8 w-full">
        Digital Deception
      </h1>
      <p className={`${styles.paragraph} :max-w-[490px]`}> Auth Insurance is your reliable safeguard against deepfakes, misinformation, 
        and disinformation.</p>
    </div>
    <div>
      <img src={robot} alt="robot" className="w-[85%] h-[85%] -mb-8 relative z-[5] "/>
      <div className="absolute z-[0] w-[40%] h-[35%] top-0 pink__gradient" />
    </div>
  </section>
)
    


export default Hero