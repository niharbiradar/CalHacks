import styles, { layout } from '../style';
import Button from './Button';

const CardDeal = () => (
  <section className={layout.section}>
    <div className={layout.sectionInfo}>
      <h2 className={styles.heading2}>Can You Afford <br className="sm:block hidden" />The Risk?</h2>
      <p className={`white-text`}>Security & Peace of Mind is just clicks away!</p>
      <Button/>
    </div>
    <div>
    
    </div>
  </section>
)

export default CardDeal