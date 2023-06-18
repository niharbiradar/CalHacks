import styles from '../style';

const DashHero = () => (
  <section id="dashboard" className={`flex  ${styles.paddingY}`}>
    <div className={`flex-1 ${styles.flexStart} flex-col xl:px-0 sm:px-16 px-6 -mb-3`}>
        <h1 className=" font-poppins font-semibold ss:text-[72px] text-[52px] text-white ss:leading-[100px] -mb-10 leading-[75px]">
          Content Dashboard
        </h1>
      </div>
  </section>
)
    


export default DashHero