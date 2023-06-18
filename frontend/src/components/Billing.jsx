import { bill } from '../assets';
import styles, { layout } from '../style';

const Billing = () => (
  <section id="product" className={layout.sectionReverse}>
    <div className={layout.sectionImgReverse}>
      <img src={bill} alt="billing" className="w-[100%] h-[100%] relative z-[5]" />
    
    <div className="absolute z-[3] -left-1/2 top-0 w-[50%] h-[50%] rounded-full white__gradient"/>
    <div className="absolute z-[0] -left-1/2 top-0 w-[50%] h-[50%] rounded-full pink__gradient"/>
    </div>
    <div className={layout.sectionInfo}>
      <h2 className={styles.heading2}>Easily Control your <br className="sm:block hidden"/> billing & Invoicing.</h2>
      <p className={`${styles.paragraph} max-w-[470px] mt-5`}>
      Stand with us on the frontlines of this technological warfare, as we work tirelessly to uphold truth, safeguard reputations, and restore trust in the world of digital communication. With our AI expertise by your side, deepfakes will find no quarter.
      </p>
    </div>
  </section>
)


export default Billing