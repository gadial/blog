---
title: "בעקבות השערת הרצף, חלק ז': המשפט היסודי של תורת הכפיה (המקרה הפרטי שהוא עיקר העבודה)"
layout: post
categories:
  - תורת הקבוצות
tags:
  - השערת הרצף
image: "/assets/img/main/forcing.png"
---


<h2>מבוא</h2>

בפוסט הקודם ראינו את ההגדרה המרכזית של תורת הכפיה, והפעם נראה את המשפט המרכזי של תורת הכפיה. ההגדרה המרכזית הייתה האופן שבו בהינתן ה"עולם" {% equation %}\mathcal{M}{% endequation %} שלנו ואידאל גנרי {% equation %}G{% endequation %} בו, אנחנו בונים מתוכם את ההרחבה {% equation %}\mathcal{M}\left[G\right]{% endequation %}, שהיא קבוצה שמכילה את {% equation %}\mathcal{M}{% endequation %} ואת {% equation %}G{% endequation %} (את אלו ראינו) ומקיימת את אותן תכונות יפות כמו {% equation %}\mathcal{M}{% endequation %}: היא בת מניה, טרנזיטיבית ומקיימת את אקסיומות ZFC.

כזכור, {% equation %}\mathcal{M}\left[G\right]{% endequation %} נבנתה בתהליך דו-שלבי. בשלב הראשון הגדרנו משהו שנקרא שמות-{% equation %}P{% endequation %}, ובשלב השני לכל שם-{% equation %}P{% endequation %} {% equation %}\sigma{% endequation %} התאמנו ערך {% equation %}\sigma^{G}{% endequation %} והגדרנו את {% equation %}\mathcal{M}\left[G\right]{% endequation %} בתור הקבוצה של כל ה-{% equation %}\sigma^{G}{% endequation %} הללו לכל שמות ה-{% equation %}P{% endequation %} הקיימים מעל {% equation %}\mathcal{M}{% endequation %}. הבניה של שמות ה-{% equation %}P{% endequation %} וההגדרה של השמת הערך עבורם היו רקורסיביים. שם-{% equation %}P{% endequation %} {% equation %}\tau{% endequation %} היה קבוצה של זוגות מהצורה {% equation %}\left(\sigma,p\right){% endequation %} כך ש-{% equation %}p\in P{% endequation %} ואילו {% equation %}\sigma{% endequation %} הוא שם-{% equation %}P{% endequation %} שכבר הוגדר קודם, ובנוסף הייתה לנו דרישה לפיה אם {% equation %}q{% endequation %} הוא הרחבה של {% equation %}p{% endequation %} וגם {% equation %}\left(\sigma,p\right)\in\tau{% endequation %} אז {% equation %}\left(\sigma,q\right)\in\tau{% endequation %}. ההגדרה של השמת ערך הייתה {% equation %}\tau^{G}=\left\{ \sigma^{G}\ |\ \exists p\in G:\left(\sigma,p\right)\in\tau\right\} {% endequation %}.

עבור הבניה הזו ראינו איך מתקיימות חלק מהאקסיומות: היקפיות, זיווג, איחוד, אינסוף ויסוד. עד כאן הכל טוב, אבל בשביל לטפל ביתר האקסיומות אני צריך משהו חזק יותר. <strong>הרבה יותר</strong>.

המשהו הזה כל כך חזק שהוא נקרא <strong>המשפט היסודי של תורת הכפיה</strong> והוא אומר, בגדול, שקבוצת תנאי הכפיה {% equation %}P{% endequation %} קובעת את המבנה {% equation %}\mathcal{M}\left[G\right]{% endequation %} בצורה כל כך חזקה, שעבור כל נוסחה {% equation %}\phi\left(\tau_{1},\ldots,\tau_{n}\right){% endequation %} קיים תנאי כפיה {% equation %}p{% endequation %} כך ש<strong>לכל</strong> {% equation %}G{% endequation %} שמכיל את {% equation %}p{% endequation %}, אנו יודעים ש-{% equation %}\mathcal{M}\left[G\right]{% endequation %} יספק את {% equation %}\phi{% endequation %}. במילים אחרות, תנאי הכפיה הבודד {% equation %}p\in G{% endequation %} <strong>כופה</strong> על {% equation %}\mathcal{M}\left[G\right]{% endequation %} לקיים את הנוסחה.

להבין את הניסוח המדויק של המשפט יכול להיות קצת מעצבן, אז בואו נפתח עם דוגמא - דוגמא חשובה במיוחד, כי היא מצד אחד המקרה הפרטי הבסיסי ביותר של המשפט, ומצד שני ההוכחה שלה תהיה החלק הקשה ביותר בהוכחה של המשפט כולו והיא תתפרש על כל הפוסט הזה ותדרוש הרבה פרטים טכניים. הדוגמא היא הנוסחה האטומית {% equation %}x_{1}=x_{2}{% endequation %}.

הנוסחה האטומית הזו כוללת שני <strong>משתנים חופשיים</strong>, {% equation %}x_{1},x_{2}{% endequation %}. אין לה ערך אמת בפני עצמה ב-{% equation %}\mathcal{M}\left[G\right]{% endequation %}; אנחנו צריכים לבחור השמה של ערכים לשני המשתנים הללו. השמה פירושה לבחור איברים של {% equation %}\mathcal{M}\left[G\right]{% endequation %} ולהציב אותם בנוסחה במקום המשתנים, כלומר נקבל משהו כמו {% equation %}\tau_{1}^{G}=\tau_{2}^{G}{% endequation %}, וזו טענה שיכולה להיות נכונה <strong>אך ורק</strong> אם {% equation %}\tau_{1}^{G}{% endequation %} ו-{% equation %}\tau_{2}^{G}{% endequation %} הם אותם איברים <strong>בדיוק</strong>. אז איפה בעצם נכנסים תנאי הכפייה לתמונה? מה המשפט פה בכלל?

בשביל לראות את זה צריך לקחת צעד אחורה ולא לחשוב על {% equation %}\mathcal{M}\left[G\right]{% endequation %} בתור משהו קבוע. השאלה שאנחנו שואלים את עצמנו עכשיו היא - עבור ערכים שונים של {% equation %}G{% endequation %}, מה קובע האם הנוסחה תתקיים? אבל גם זו נדמית כמו שאלה חסרת משמעות: הנוסחה {% equation %}x_{1}=x_{2}{% endequation %} מתקיימת אם ורק אם מציבים בשני המשתנים שלה את אותו איבר, סוף הסיפור.

לכן אנחנו שואלים שאלה קצת שונה. אנחנו מתחילים עם שני שמות-{% equation %}P{% endequation %}, {% equation %}\tau_{1},\tau_{2}{% endequation %}. בפני עצמם, השמות הללו הם בסך הכל איברים של {% equation %}\mathcal{M}{% endequation %}. אם נבחר {% equation %}G{% endequation %} נוכל להעביר אותם תהליך של השמה שיחזיר מהם ערך שהוא איבר ב-{% equation %}\mathcal{M}\left[G\right]{% endequation %}, אבל הם קיימים גם בלי שיהיה {% equation %}G{% endequation %} אחד ספציפי ברקע. עכשיו אני יכול "להציב" אותם ב-{% equation %}x_{1}=x_{2}{% endequation %} ולקבל את הנוסחה {% equation %}\tau_{1}=\tau_{2}{% endequation %}. אני חושב על זה בתור סימון בלבד, מין תבנית שמחכה שנבחר {% equation %}G{% endequation %} ספציפי ואז נקבל מהנוסחה הזו את {% equation %}\tau_{1}^{G}=\tau_{2}^{G}{% endequation %}. והשאלה שאנחנו שואלים היא: מה צריך {% equation %}G{% endequation %} לקיים כדי שהנוסחה {% equation %}\tau_{1}^{G}=\tau_{2}^{G}{% endequation %} תהיה בעלת ערך T? התשובה היא שעבור {% equation %}\tau_{1},\tau_{2}{% endequation %} הללו קיים תנאי כפיה {% equation %}p{% endequation %} כך שאם {% equation %}p\in G{% endequation %}, מובטח ש-{% equation %}\tau_{1}^{G}=\tau_{2}^{G}{% endequation %} היא אכן בעלת ערך T.

בואו נעבור לנסח את זה פורמלית, ולהבין איך בכלל תלך ההוכחה.

<h2>מנסחים את זה פורמלית ומבינים איך בכלל הולכת ההוכחה</h2>

מושג המפתח שעליו אנחנו מדברים כאן הוא מתי תנאי כפיה {% equation %}p{% endequation %} <strong>כופה</strong> משהו על נוסחה ושמות-{% equation %}P{% endequation %} שמופיעים בה. אז תהא {% equation %}\phi\left(x_{1},\ldots,x_{n}\right){% endequation %} נוסחה כלשהי עם משתנים חופשיים {% equation %}x_{1},\ldots,x_{n}{% endequation %} ויהיו {% equation %}\tau_{1},\ldots,\tau_{n}{% endequation %} שמות-{% equation %}P{% endequation %} כלשהם, ויהא {% equation %}p\in P{% endequation %} תנאי כפיה כלשהו. אני אגיד ש-{% equation %}p{% endequation %} <strong>כופה</strong> את {% equation %}\phi\left(\tau_{1},\ldots,\tau_{n}\right){% endequation %} ואסמן זאת {% equation %}p\Vdash\phi\left(\tau_{1},\ldots,\tau_{n}\right){% endequation %} אם <strong>לכל</strong> אידאל גנרי {% equation %}G{% endequation %} כך ש-{% equation %}p\in G{% endequation %}, מתקיים ש-{% equation %}\mathcal{M}\left[G\right]\models\phi\left(\tau_{1}^{G},\ldots,\tau_{n}^{G}\right){% endequation %}, דהיינו הפסוק {% equation %}\phi\left(x_{1},\ldots,x_{n}\right){% endequation %} מקבל ערך T במודל של {% equation %}\mathcal{M}\left[G\right]{% endequation %} תחת ההשמה שנותנת למשתנים את הערכים {% equation %}\tau_{1}^{G},\ldots,\tau_{n}^{G}{% endequation %} (שימו לב: ב-{% equation %}\phi{% endequation %} יכולים להיות גם משתנים מכומתים, והרעיון הוא שהערכים המכומתים הללו מגיעים מתוך {% equation %}\mathcal{M}\left[G\right]{% endequation %}). הנקודה העדינה שצריך לשים לב אליה היא שכפיה לא תלויה רק בתנאי {% equation %}p{% endequation %} ובפסוק {% equation %}\phi{% endequation %} אלא גם <strong>בשמות ספציפיים</strong> {% equation %}\tau_{1},\ldots,\tau_{n}{% endequation %}, כלומר {% equation %}p{% endequation %} לא סתם כופה את הפסוק {% equation %}\phi{% endequation %} אלא את ה"תבנית" {% equation %}\phi\left(\tau_{1},\ldots,\tau_{n}\right){% endequation %} שהיא ערבוב של הפסוק והשמות.

המשפט הכללי שאני רוצה להוכיח - "המשפט היסודי של תורת הכפיה", הוא זה: לכל אידאל גנרי {% equation %}G{% endequation %}, נוסחה {% equation %}\phi\left(x_{1},\ldots,x_{n}\right){% endequation %} ושמות-{% equation %}P{% endequation %} {% equation %}\tau_{1},\ldots,\tau_{n}{% endequation %}, מתקיים ש-{% equation %}\mathcal{M}\left[G\right]\models\phi\left(\tau_{1}^{G},\ldots,\tau_{n}^{G}\right){% endequation %} אם ורק אם קיים {% equation %}p\in G{% endequation %} כך ש-{% equation %}p{% endequation %} כופה את {% equation %}\phi\left(\tau_{1},\ldots,\tau_{n}\right){% endequation %}. בניסוח הפורמלי המלא בפוסט הבא יהיה עוד חלק חשוב לא פחות שעוסק ביכולת שלנו להגדיר את יחס הכפיה במסגרת {% equation %}\mathcal{M}{% endequation %}, אבל בינתיים אני חושב שזה יכול רק לבלבל אז בואו נראה איך זה צץ מעצמו כשאנחנו מוכיחים את המשפט.

כיוון אחד של המשפט הוא טריוויאלי: מן הסתם אם יש ב-{% equation %}G{% endequation %} איבר {% equation %}p{% endequation %} שכופה את {% equation %}\phi\left(\tau_{1},\ldots,\tau_{n}\right){% endequation %} אז נובע מכך מייד ש-{% equation %}\mathcal{M}\left[G\right]\models\phi\left(\tau_{1}^{G},\ldots,\tau_{n}^{G}\right){% endequation %} כי זה נובע מיידית מההגדרה של {% equation %}p\Vdash\phi\left(\tau_{1},\ldots,\tau_{n}\right){% endequation %}. מה שמעניין הוא הכיוון השני: שאם {% equation %}\phi\left(\tau_{1}^{G},\ldots,\tau_{n}^{G}\right){% endequation %} מקבלת T במודל הספציפי {% equation %}\mathcal{M}\left[G\right]{% endequation %}, זה אומר שאפשר "לזקק" את {% equation %}G{% endequation %} לכדי איבר בודד {% equation %}p\in G{% endequation %} שהוא זה שאחראי לזה.

כרגע אני רוצה להסתפק ביעד הצנוע של להוכיח את זה עבור הנוסחה {% equation %}x_{1}=x_{2}{% endequation %}. כלומר, יהיו {% equation %}\tau_{1},\tau_{2}{% endequation %} שני שמות-{% equation %}P{% endequation %}; אני רוצה להראות שאם עבור אידאל גנרי {% equation %}G{% endequation %} מתקיים {% equation %}\tau_{1}^{G}=\tau_{2}^{G}{% endequation %} , אז קיים {% equation %}p\in G{% endequation %} כך ש-{% equation %}p\Vdash\tau_{1}=\tau_{2}{% endequation %}, דהיינו <strong>לכל</strong> אידאל גנרי {% equation %}G^{\prime}{% endequation %} כך ש-{% equation %}p\in G^{\prime}{% endequation %} יתקיים {% equation %}\tau_{1}^{G^{\prime}}=\tau_{2}^{G^{\prime}}{% endequation %}. זו המטרה, וזו לא תהיה מטרה קלה בכלל, אבל נסתדר.

לפני שמדברים על מה קורה בתוך אידאלים גנריים, אנחנו צריכים לענות לשאלה יותר בסיסית - האם אנחנו יכולים, עבור {% equation %}\tau_{1},\tau_{2}{% endequation %}, "לתפוס" את אותם {% equation %}p{% endequation %}-ים שכופים את השוויון שלהם? זה יצריך מאיתנו בניה לא טריוויאלית וזהירה, אבל התשובה היא <strong>כן</strong>.

כזכור, את שמות ה-{% equation %}P{% endequation %} בנינו באופן היררכי; בנינו סדרה {% equation %}N_{\alpha}{% endequation %} של קבוצות, שמאונדקסות על ידי הסודרים שמופיעים ב-{% equation %}\mathcal{M}{% endequation %}, כך שכל שם-{% equation %}P{% endequation %} השתייך לאחת הקבוצות. <strong>הדרגה</strong> של שם-{% equation %}P{% endequation %} הייתה האינדקס המינימלי {% equation %}\alpha{% endequation %} של קבוצה כזו שבה הוא מופיע; האיברים שלו התבססו על שמות-{% equation %}P{% endequation %} מדרגה נמוכה יותר. בהיררכייה הזו נשתמש כדי ליצור את ה<strong>יחס</strong> {% equation %}p\Vdash\tau_{1}=\tau_{2}{% endequation %}. יחס כזה הוא אוסף של <strong>שלשות</strong> מהצורה {% equation %}\left(p,\tau_{1},\tau_{2}\right){% endequation %}; ונבנה את אוסף השלשות הזה בצורה רקורסיבית. לכל סודר {% equation %}\alpha\in\mathcal{M}{% endequation %} נגדיר קבוצה {% equation %}\mathcal{F}_{\alpha}{% endequation %} שכוללת חלק מהשלשות הללו, בהתאם לדרגה של {% equation %}\tau_{1},\tau_{2}{% endequation %}. פורמלית, {% equation %}\mathcal{F}_{\alpha}\subseteq P\times N_{\alpha}\times N_{\alpha}{% endequation %}, כלומר ב-{% equation %}\mathcal{F}_{\alpha}{% endequation %} יופיעו אותם שמות-{% equation %}P{% endequation %} שהם לכל היותר מדרגה {% equation %}\alpha{% endequation %}.

בואו נסמן את הדרגה של שם-{% equation %}P{% endequation %} כלשהו ב-{% equation %}\text{rank}\left(\tau\right){% endequation %} ועבור שני שמות, נסמן {% equation %}\text{rank}\left(\tau_{1},\tau_{2}\right)=\text{max}\left\{ \text{rank}\left(\tau_{1}\right),\text{rank}\left(\tau_{2}\right)\right\} {% endequation %}. עכשיו אפשר סוף סוף להגדיר פורמלית את {% equation %}\mathcal{F}_{\alpha}{% endequation %}: {% equation %}\left(p,\tau_{1},\tau_{2}\right)\in\mathcal{F}_{\alpha}{% endequation %} אם מתקיימים שני התנאים הבאים (שהם בעצם ניסוחים סימטריים של אותו דבר):

<ul> <li>לכל {% equation %}\left(\sigma_{1},q_{1}\right)\in\tau_{1}{% endequation %} כך ש-{% equation %}p\subseteq q_{1}{% endequation %}, קיים {% equation %}\left(\sigma_{2},q_{2}\right)\in\tau_{2}{% endequation %} כך ש-{% equation %}q_{1}\subseteq q_{2}{% endequation %} ו-{% equation %}\left(q_{2},\sigma_{1},\sigma_{2}\right)\in\mathcal{F}_{\text{rank}\left(\sigma_{1},\sigma_{2}\right)}{% endequation %}.</li>


<li>לכל {% equation %}\left(\sigma_{2},q_{2}\right)\in\tau_{2}{% endequation %} כך ש-{% equation %}p\subseteq q_{2}{% endequation %}, קיים {% equation %}\left(\sigma_{1},q_{1}\right)\in\tau_{1}{% endequation %} כך ש-{% equation %}q_{2}\subseteq q_{1}{% endequation %} ו-{% equation %}\left(q_{1},\sigma_{1},\sigma_{2}\right)\in\mathcal{F}_{\text{rank}\left(\sigma_{1},\sigma_{2}\right)}{% endequation %}.</li>

</ul>

לא לגמרי ברור בשלב הזה מה הרעיון בהגדרה ולמה זה עובד - נקדיש לא מעט עבודה טכנית בשביל זה. אבל בשלב הזה אפשר כבר להשתכנע שהשימוש ברקורסיה פה הוא תקין: אנחנו מגדירים את {% equation %}\mathcal{F}_{\alpha}{% endequation %} תוך הסתמכות על כך ש-{% equation %}\mathcal{F}_{\text{rank}\left(\sigma_{1},\sigma_{2}\right)}{% endequation %} כבר הוגדר לכל {% equation %}\sigma_{1},\sigma_{2}{% endequation %} שמופיעים בתוך {% equation %}\tau_{1},\tau_{2}{% endequation %} בהתאמה. זה עובד, כי {% equation %}\text{rank}\left(\sigma_{i}\right)<\text{rank}\left(\tau_{i}\right)\le\alpha{% endequation %} (ממש על פי הגדרה; שם-{% equation %}P{% endequation %} מדרגה מסוימת מוגדר על ידי אוסף זוגות שנבנים משמות שדרגתם קטנה יותר) ולכן {% equation %}\text{rank}\left(\sigma_{1},\sigma_{2}\right)<\alpha{% endequation %}.

<h2>מוכיחים שזה עובד - החימום</h2>

לפני שאני אגיע להוכחה המרכזית, אני צריך להוכיח כמה טענות עזר שיהיו קריטיות במהלכה. הן עצמן פשוטות למדי ומרגישות כמו משחק בהגדרות.

ראשית, בואו נוכיח שאם {% equation %}G{% endequation %} הוא אידאל גנרי ו-{% equation %}D\in\mathcal{M}{% endequation %} היא קבוצה {% equation %}D\subseteq P{% endequation %}, כך שלכל איבר של {% equation %}G{% endequation %}<strong> </strong>יש הרחבה משותפת עם איבר של {% equation %}D{% endequation %}, אז {% equation %}G\cap D\ne\emptyset{% endequation %} (כזכור, הרחבה משותפת של {% equation %}p_{1},p_{2}{% endequation %} היא {% equation %}q{% endequation %} כך ש-{% equation %}p_{1}\subseteq q{% endequation %} וגם {% equation %}p_{2}\subseteq q{% endequation %}).

למה הטענה נכונה? בשביל זה צריך להיזכר בהגדרה של אידאל גנרי: "אידאל {% equation %}G{% endequation %} הוא גנרי ביחס ל-{% equation %}\mathcal{M}{% endequation %} אם לכל קבוצה צפופה {% equation %}D\subseteq P{% endequation %} כך ש-{% equation %}D\in\mathcal{M}{% endequation %}, החיתוך של {% equation %}G{% endequation %} ו-{% equation %}D{% endequation %} אינו ריק, {% equation %}G\cap D\ne\emptyset{% endequation %}." רואים? הנה הגיעה לה {% equation %}D{% endequation %} וגם ה-{% equation %}G\cap D\ne\emptyset{% endequation %} המבוקש. רק צריך להראות ש-{% equation %}D{% endequation %} צפופה. ומה זה צפופה? נפלא, בואו ניזכר גם בהגדרה הזו, "תת-קבוצה {% equation %}D\subseteq P{% endequation %} היא <strong>צפופה</strong> אם לכל {% equation %}p\in P{% endequation %} קיימת הרחבה ב-{% equation %}D{% endequation %}."

אוקיי, יש לנו בעיה: ההגדרה של צפופה חזקה מדי, לא מובטח ש-{% equation %}D{% endequation %} תקיים אותה. אז בואו <strong>נרחיב</strong> את {% equation %}D{% endequation %} לקבלת קבוצה {% equation %}D^{\prime}{% endequation %} שתהיה צפופה, באופן הבא: נוסיף ל-{% equation %}D^{\prime}{% endequation %} את כל האיברים שמרחיבים איבר כלשהו ב-{% equation %}D{% endequation %}, כלומר את הקבוצה {% equation %}\left\{ q\in P\ |\ \exists p\in D:p\subseteq q\right\} {% endequation %}. לרוע המזל, גם זה לא מספיק טוב. מה עם איברים {% equation %}p\in P{% endequation %} שאין להם שום הרחבה משותפת עם אף איבר של {% equation %}D{% endequation %}? אוקיי, בואו נוסיף <strong>גם אותם</strong> אל {% equation %}D^{\prime}{% endequation %}. זה כבר מבטיח ש-{% equation %}D^{\prime}{% endequation %} צפופה, כי אם {% equation %}p\in P{% endequation %} יש שתי אפשרויות: או שאין ל-{% equation %}p{% endequation %} הרחבה משותפת עם אף איבר של {% equation %}D{% endequation %}, ואז מההגדרה הוא שייך אל {% equation %}D^{\prime}{% endequation %}; או שיש לו הרחבה משותפת ואז ההרחבה הזו כבר מצאה את דרכה אל {% equation %}D^{\prime}{% endequation %} כשרק הגדרנו אותו. קיבלנו ש-{% equation %}D^{\prime}{% endequation %} אכן צפופה ולכן {% equation %}G\cap D^{\prime}\ne\emptyset{% endequation %}.

עכשיו, אנחנו יודעים שלכל איבר של {% equation %}G{% endequation %} יש הרחבה משותפת עם איבר של {% equation %}D{% endequation %}, כלומר אם {% equation %}p\in G\cap D^{\prime}{% endequation %} אז {% equation %}p{% endequation %} שייך לחצי הראשון של {% equation %}D^{\prime}{% endequation %}, של אותם איברים שהתקבלו מהרחבת איברים של {% equation %}D{% endequation %}. זה עוזר לנו, כי אנחנו יודעים מההגדרה של אידאל שאם איבר שייך אליו, כך גם כל מי שמוכל בו:

"סגורה כלפי מטה: אם {% equation %}q\in G{% endequation %} ועבור {% equation %}p\in P{% endequation %} כלשהו מתקיים {% equation %}p\subseteq q{% endequation %} אז {% equation %}p\in G{% endequation %}."

אז במקרה שלנו, {% equation %}p{% endequation %} שייך לאידאל {% equation %}G{% endequation %} ומרחיב איבר של {% equation %}D{% endequation %} ולכן אותו איבר של {% equation %}D{% endequation %} שייך ל-{% equation %}G{% endequation %} בעצמו, וסיימנו.

עכשיו בואו נוכיח בעזרת הטענה שזה עתה ראינו עוד משהו. אני אומר על קבוצה {% equation %}D\in\mathcal{M}{% endequation %} שהיא <strong>צפופה מעל</strong> {% equation %}p{% endequation %} כלשהו אם לכל הרחבה של {% equation %}p{% endequation %} קיימת הרחבה ב-{% equation %}D{% endequation %} (כלומר לכל {% equation %}p\subseteq q{% endequation %} קיים {% equation %}q^{\prime}\in D{% endequation %} כך ש-{% equation %}q\subseteq q^{\prime}{% endequation %}). זו גרסה מקומית של ההגדרה הכללית של צפיפות שפשוט דרשה שלכל איבר תהיה הרחבה ששייכת ל-{% equation %}D{% endequation %}.

עכשיו, אם {% equation %}G{% endequation %} הוא אידאל גנרי ו-{% equation %}D{% endequation %} צפופה מעל {% equation %}p\in G{% endequation %} כלשהו, אני רוצה להסיק מכך ש-{% equation %}G\cap D\ne\emptyset{% endequation %}. אז מן הסתם אנסה לבצע רדוקציה לטענה הקודמת, מה שמצריך אותי להוכיח שלכל איבר של {% equation %}G{% endequation %} יש הרחבה משותפת עם איבר של {% equation %}D{% endequation %}. אבל זה קל, כי בואו ניקח {% equation %}p^{\prime}\in G{% endequation %}. מההגדרה של אידאל קיים {% equation %}q\in G{% endequation %} כך ש-{% equation %}p,p^{\prime}\subseteq q{% endequation %}, ולכן אנחנו יודעים שיש {% equation %}q^{\prime}\in D{% endequation %} כך ש-{% equation %}p^{\prime}\subseteq q\subseteq q^{\prime}{% endequation %} וה-{% equation %}q^{\prime}{% endequation %} הזה הוא הרחבה משותפת של {% equation %}p^{\prime}{% endequation %} ושל עצמו. לכן אפשר להסיק ש-{% equation %}G\cap D\ne\emptyset{% endequation %}.

לבסוף, עוד דבר אחד שאזדקק לו הוא זה: שאם {% equation %}G\subseteq A\in\mathcal{M}{% endequation %} אז קיים {% equation %}p\in G{% endequation %} כך שכל הרחבה של {% equation %}p{% endequation %} שייכת ל-{% equation %}A{% endequation %}. בשלב הזה אנחנו כנראה לא מספיק בהכרה כדי "להרגיש" מה זה אומר בכלל, אבל כשאני חושב על זה רגע זה לא משהו מובן מאליו. הרחבות של איברים הן בדרך כלל משהו שמתפרע לו ואין לנו שליטה עליו, לא? באידאל ה"שליטה" שיש לנו היא לכיוון ההפוך - אם איבר שייך לאידאל, אז כל מי שהוא מרחיב גם כן שייך לאידאל. כאן סוג של קורה הכיוון השני, כך שזה מעין קסם. הסיבה לקסם הזה היא ש-{% equation %}A\in\mathcal{M}{% endequation %} וזה איכשהו מבטיח שהמבנה שלו יהיה "נחמד" מספיק, להבדיל מהמבנה היותר מסובך של {% equation %}G{% endequation %} שגורם לכך ש-{% equation %}G{% endequation %} לא תהיה ב-{% equation %}\mathcal{M}{% endequation %}.

אוקיי, אז איך מוכיחים את זה? מכיוון ש-{% equation %}G\subseteq A{% endequation %} אז {% equation %}G\cap P\backslash A=\emptyset{% endequation %}. ראינו לפני רגע את הטענה שאם {% equation %}D\in\mathcal{M}{% endequation %} היא קבוצה {% equation %}D\subseteq P{% endequation %}, כך שלכל איבר של {% equation %}G{% endequation %}<strong> </strong>יש הרחבה משותפת עם איבר של {% equation %}D{% endequation %}, אז {% equation %}G\cap D\ne\emptyset{% endequation %}. במקרה שלנו ניקח {% equation %}D=P\backslash A{% endequation %} (מכיוון ש-{% equation %}P,A\in\mathcal{M}{% endequation %} ו-{% equation %}\mathcal{M}{% endequation %} מקיימת את ZFC אז גם {% equation %}P\backslash A\in\mathcal{M}{% endequation %}) ולכן מכך שהטענה <strong>לא</strong> מתקיימת נוכל להסיק את השלילה של התנאים שלה, כלומר ש<strong>קיים</strong> איבר {% equation %}p\in G{% endequation %} ש<strong>אין</strong> לו הרחבה משותפת עם אף איבר של {% equation %}D{% endequation %}. זה כמובן ה-{% equation %}p{% endequation %} שאנחנו רוצים; כל הרחבה של {% equation %}p{% endequation %} הזה בהכרח לא שייכת ל-{% equation %}D{% endequation %} אחרת היינו מקבלים הרחבה משותפת ל-{% equation %}p{% endequation %} ולאיבר של {% equation %}D{% endequation %} (הוא עצמו). המסקנה היא ש-{% equation %}p\in A{% endequation %} ובכך סיימנו את ההוכחה של טענות העזר ואפשר לעבור להוכחה של המשפט המרכזי.

<h2>מוכיחים שזה עובד - ההוכחה</h2>

הנה המשפט שאני רוצה להוכיח. אני אוכיח אותו באינדוקציה על הסודרים של {% equation %}\mathcal{M}{% endequation %}, והוא כולל שני חלקים, שכל אחד מהם, כשמשתמשים בו בתור הנחת האינדוקציה, עוזר להוכיח את השני. הנה מה שהוא אומר:

בהינתן סודר {% equation %}\alpha\in\mathcal{M}{% endequation %}, לכל זוג שמות-{% equation %}P{% endequation %} {% equation %}\tau_{1},\tau_{2}{% endequation %} שהם מדרגה {% equation %}\alpha{% endequation %} לכל היותר, מתקיים:

<ol> <li>אידאל גנרי {% equation %}G{% endequation %} של {% equation %}P{% endequation %} מקיים {% equation %}\tau_{1}^{G}=\tau_{2}^{G}{% endequation %} אם ורק אם קיים {% equation %}p\in G{% endequation %} שכופה את {% equation %}\tau_{1}=\tau_{2}{% endequation %}.</li>


<li>איבר {% equation %}p\in P{% endequation %} כופה את {% equation %}\tau_{1}=\tau_{2}{% endequation %} אם ורק אם {% equation %}\left(p,\tau_{1},\tau_{2}\right)\in\mathcal{F}_{\alpha}{% endequation %}</li>

</ol>

כאמור, ההוכחה תהיה באינדוקציה; אנחנו נוכל להניח שהטענה הוכחה לכל זוג {% equation %}\sigma_{1},\sigma_{2}{% endequation %} של שמות שהם מדרגה נמוכה מ-{% equation %}\alpha{% endequation %} (כלומר, כל שם שמופיע ב-{% equation %}\tau_{1}{% endequation %} או {% equation %}\tau_{2}{% endequation %}). תחת ההנחה הזו, אני הולך להוכיח טענת עזר שהיא הדבר המרכזי שנזדקק לו כאן, ומן הסתם תתבסס על הטענות שהוכחנו בחלק של "החימום". אני אגדיר קבוצה {% equation %}A\subseteq P{% endequation %} באופן הבא: {% equation %}q_{1}\in A{% endequation %} אם לכל {% equation %}\sigma_{1}{% endequation %} כך ש-{% equation %}\left(\sigma_{1},q_{1}\right)\in\tau_{1}{% endequation %} קיים {% equation %}\left(\sigma_{2},\tau_{2}\right)\in\tau_{2}{% endequation %} כך ש-{% equation %}q_{1}\subseteq q_{2}{% endequation %} ו-{% equation %}q_{2}{% endequation %} כופה את {% equation %}\sigma_{1}=\sigma_{2}{% endequation %}. עכשיו אני טוען ש-{% equation %}A{% endequation %} מקיימת את שתי התכונות הבאות, לכל אידאל גנרי {% equation %}G{% endequation %}:

<ul> <li>אם {% equation %}\tau_{1}^{G}\subseteq\tau_{2}^{G}{% endequation %} אז {% equation %}G\subseteq A{% endequation %}.</li>


<li>אם יש {% equation %}p\in G{% endequation %} שכל הרחבה שלו שייכת ל-{% equation %}A{% endequation %}, אז {% equation %}\tau_{1}^{G}\subseteq\tau_{2}^{G}{% endequation %}.</li>

</ul>

במקום להוכיח את שתי התכונות הללו מייד, בואו נראה איך הן משמשות אותנו להוכחת המשפט המרכזי, כי בלי זה לא ברור למה הן כאן בכלל ובשביל מה כל זה טוב.

ראשית בואו נטפל בהוכחה של טענה 1. כבר אמרנו שכיוון אחד טריוויאלי: אם קיים {% equation %}p\in G{% endequation %} שכופה את {% equation %}\tau_{1}=\tau_{2}{% endequation %} אז בוודאי ש-{% equation %}G{% endequation %} מקיים {% equation %}\tau_{1}^{G}=\tau_{2}^{G}{% endequation %} (וזה מתקיים <strong>לכל</strong> אידאל שיכיל את {% equation %}p{% endequation %} הזה, לא רק {% equation %}G{% endequation %}). אז מה שמעניין אותנו הוא הכיוון השני, זה שבשבילו הכנסנו לתמונה את ההגדרה של {% equation %}\mathcal{F}_{\alpha}{% endequation %} מלכתחילה: איך אני הולך למצוא את ה-{% equation %}p{% endequation %} הכופה הקסום הזה, רק מתוך הידיעה ש-{% equation %}\tau_{1}^{G}=\tau_{2}^{G}{% endequation %}?

ובכן, טענת העזר נחלצת לעזרתנו: {% equation %}\tau_{1}^{G}=\tau_{2}^{G}{% endequation %} בפרט אומר {% equation %}\tau_{1}^{G}\subseteq\tau_{2}^{G}{% endequation %}, ולכן ש-{% equation %}G\subseteq A{% endequation %}. עכשיו הנה עניין טיפה טריקי שאנפנף בו בידיים: אני טוען ש-{% equation %}A\in\mathcal{M}{% endequation %} (השייכות הזו ל-{% equation %}\mathcal{M}{% endequation %} הייתה קריטית בטענות העזר). למה? כי אפשר להגדיר את {% equation %}A{% endequation %} באמצעות הנוסחה

{% equation %}A=\left\{ q_{1}\in P:\forall\sigma_{1}\left(\sigma_{1},q_{1}\right)\in\tau_{1}\to\exists\left(\sigma_{2},q_{2}\right)\in\tau_{2}\left(q_{1}\subseteq q_{2}\wedge q_{2}\Vdash\sigma_{1}=\sigma_{2}\right)\right\} {% endequation %}

כלומר, אני יכול לקבל את {% equation %}A{% endequation %} בעזרת אקסיומת ההפרדה, בתנאי שאפשר לנסח את כל התנאי המסובך של הקבוצה במסגרת {% equation %}\mathcal{M}{% endequation %}. מה שלא ברור שאפשר לנסח הוא {% equation %}q_{2}\Vdash\sigma_{1}=\sigma_{2}{% endequation %}, התנאי שאומר "{% equation %}q_{2}{% endequation %} כופה את {% equation %}\sigma_{1}=\sigma_{2}{% endequation %}", אבל כאן נחלצת לעזרתי הנחת האינדוקציה שאומרת שזה קורה אם ורק אם {% equation %}\left(q_{2},\sigma_{1},\sigma_{2}\right)\in\mathcal{F}_{\beta}{% endequation %} עבור {% equation %}\beta<\alpha{% endequation %} כלשהו, ואת זה אפשר להגדיר במסגרת {% equation %}\mathcal{M}{% endequation %}.

עכשיו, מכיוון ש-{% equation %}G\subseteq A\in\mathcal{M}{% endequation %} אז מהטענה שראינו קודם קיים {% equation %}p\in G{% endequation %} כך שכל הרחבה של {% equation %}p{% endequation %} שייכת ל-{% equation %}A{% endequation %}. עכשיו מגיע החלק הקסום. כזכור, אני מבטיח שאוכיח את הטענה הבאה על {% equation %}A{% endequation %}:

<ul> <li>אם יש {% equation %}p\in G{% endequation %} שכל הרחבה שלו שייכת ל-{% equation %}A{% endequation %}, אז {% equation %}\tau_{1}^{G}\subseteq\tau_{2}^{G}{% endequation %}.</li>

</ul>

העניין הוא שהטענה הזו נכונה <strong>לכל</strong> אידאל גנרי {% equation %}G{% endequation %} שמכיל את {% equation %}G{% endequation %}, לא רק לאידאל שהתחלנו ממנו את הכיוון הזה של ההוכחה. זו בדיוק הקפיצה שמאפשרת לנו לעבור מ-"מתקיים {% equation %}\tau_{1}^{G}=\tau_{2}^{G}{% endequation %}" אל "יש איבר שכופה את {% equation %}\tau_{1}=\tau_{2}{% endequation %}". פורמלית, ניקח {% equation %}G^{\prime}{% endequation %} כלשהו כך ש-{% equation %}p\in G^{\prime}{% endequation %}, אז מכיוון שכל הרחבה של {% equation %}p{% endequation %} שייכת ל-{% equation %}A{% endequation %}, קיבלנו ש-{% equation %}\tau_{1}^{G^{\prime}}\subseteq\tau_{2}^{G^{\prime}}{% endequation %}. המסקנה? {% equation %}p{% endequation %} כופה את {% equation %}\tau_{1}\subseteq\tau_{2}{% endequation %} שזה... לא בדיוק מה שרצינו, אבל זה קרוב מאוד.

בואו נחדד את מה שהוכחנו: ראינו שאם {% equation %}\tau_{1}^{G}=\tau_{2}^{G}{% endequation %} אז קיים {% equation %}p_{1}\in G{% endequation %} שכופה את {% equation %}\tau_{1}\subseteq\tau_{2}{% endequation %}. באופן סימטרי לגמרי קיים {% equation %}p_{2}\in G{% endequation %} שכופה את {% equation %}\tau_{2}\subseteq\tau_{1}{% endequation %} (ומוכיחים את זה דרך קבוצה {% equation %}A{% endequation %} שונה, "של {% equation %}p_{2}{% endequation %}"). מכיוון ש-{% equation %}G{% endequation %} הוא אידאל, קיים {% equation %}p\in G{% endequation %} כך ש-{% equation %}p_{1},p_{2}\subseteq p{% endequation %}. כל הרחבה של {% equation %}p{% endequation %} הזה היא גם הרחבה של {% equation %}p_{1}{% endequation %} ולכן שייכת ל-{% equation %}A{% endequation %} של {% equation %}p_{1}{% endequation %}. לכן גם {% equation %}p{% endequation %} כופה את {% equation %}\tau_{1}\subseteq\tau_{2}{% endequation %}, ובאותו אופן הוא גם כופה את {% equation %}\tau_{2}\subseteq\tau_{1}{% endequation %} ומשני אלו קיבלנו שהוא כופה את {% equation %}\tau_{1}=\tau_{2}{% endequation %}, וזה בדיוק מה שרצינו!

אבל לא סיימנו את ההוכחה עדיין, כי צריך להוכיח גם את חלק 2 של המשפט:

<ul> <li>איבר {% equation %}p\in P{% endequation %} כופה את {% equation %}\tau_{1}=\tau_{2}{% endequation %} אם ורק אם {% equation %}\left(p,\tau_{1},\tau_{2}\right)\in\mathcal{F}_{\alpha}{% endequation %}</li>

</ul>

החלק הזה היה קריטי עבורנו קודם, בשלב שבו רצינו להוכיח ש-{% equation %}A\in\mathcal{M}{% endequation %}. באותו אופן, ההוכחה של החלק הזה תסתמך אינדוקטיבית על מה שזה עתה הוכחנו:

<ul> <li>אידאל גנרי {% equation %}G{% endequation %} של {% equation %}P{% endequation %} מקיים {% equation %}\tau_{1}^{G}=\tau_{2}^{G}{% endequation %} אם ורק אם קיים {% equation %}p\in G{% endequation %} שכופה את {% equation %}\tau_{1}=\tau_{2}{% endequation %}.</li>

</ul>

בואו נראה איך. כאן יש לנו שני כיוונים שאף אחד מהם לא טריוויאלי לגמרי. ראשית נניח ש-{% equation %}p{% endequation %} כופה את {% equation %}\tau_{1}=\tau_{2}{% endequation %} ונוכיח ש-{% equation %}\left(p,\tau_{1},\tau_{2}\right)\in\mathcal{F}_{\alpha}{% endequation %}. כזכור, שייכות ליחס הזה דורשת שתי טענות סימטריות כך שמספיק לי להוכיח את הראשונה, שהיא

<ul> <li>לכל {% equation %}\left(\sigma_{1},q_{1}\right)\in\tau_{1}{% endequation %} כך ש-{% equation %}p\subseteq q_{1}{% endequation %}, קיים {% equation %}\left(\sigma_{2},q_{2}\right)\in\tau_{2}{% endequation %} כך ש-{% equation %}q_{1}\subseteq q_{2}{% endequation %} ו-{% equation %}\left(q_{2},\sigma_{1},\sigma_{2}\right)\in\mathcal{F}_{\text{rank}\left(\sigma_{1},\sigma_{2}\right)}{% endequation %}</li>

</ul>

התנאי הזה דומה באופן מובהק ולא מקרי בעליל להגדרה של {% equation %}A{% endequation %}:

<ul> <li>{% equation %}q_{1}\in A{% endequation %} אם לכל {% equation %}\sigma_{1}{% endequation %} כך ש-{% equation %}\left(\sigma_{1},q_{1}\right)\in\tau_{1}{% endequation %} קיים {% equation %}\left(\sigma_{2},\tau_{2}\right)\in\tau_{2}{% endequation %} כך ש-{% equation %}q_{1}\subseteq q_{2}{% endequation %} ו-{% equation %}q_{2}{% endequation %} כופה את {% equation %}\sigma_{1}=\sigma_{2}{% endequation %}.</li>

</ul>

ליתר דיוק, התנאי של שייכות ל-{% equation %}\mathcal{F}_{\alpha}{% endequation %} בעצם אומר "לכל הרחבה {% equation %}q_{1}{% endequation %} של {% equation %}p{% endequation %}, מתקיים ש-{% equation %}q_{1}\in A{% endequation %}" (אני משתמש כאן בהנחת האינדוקציה במובלע כשאני מתייחס אל {% equation %}\left(q_{2},\sigma_{1},\sigma_{2}\right)\in\mathcal{F}_{\text{rank}\left(\sigma_{1},\sigma_{2}\right)}{% endequation %} בתור "{% equation %}q_{2}{% endequation %} כופה את {% equation %}\sigma_{1}=\sigma_{2}{% endequation %}"). זה מה שאנחנו רוצים להוכיח. לשם כך אני אגייס את אחת מהתכונות של {% equation %}A{% endequation %} שהבטחתי להוכיח וטרם עשיתי זאת:

<ul> <li>אם {% equation %}\tau_{1}^{G}\subseteq\tau_{2}^{G}{% endequation %} אז {% equation %}G\subseteq A{% endequation %}.</li>

</ul>

המהלך הלוגי הוא כזה: ניקח הרחבה {% equation %}q_{1}{% endequation %} כלשהי של {% equation %}p{% endequation %}. אם {% equation %}G{% endequation %} הוא אידאל גנרי כך ש-{% equation %}q_{1}\in G{% endequation %} אז בגלל תכונת הסגירות מטה של אידאלים, {% equation %}p\in G{% endequation %}. מכיוון ש-{% equation %}p{% endequation %} כופה את {% equation %}\tau_{1}=\tau_{2}{% endequation %} הרי ש-{% equation %}\tau_{1}^{G}\subseteq\tau_{2}^{G}{% endequation %} ולכן {% equation %}q_{1}\in G\subseteq A{% endequation %} וקיבלנו ש-{% equation %}q_{1}\in A{% endequation %}, מה שמסיים את הכיוון הזה... אבל רק אם <strong>קיים</strong> אידאל גנרי {% equation %}G{% endequation %} כך ש-{% equation %}q_{1}\in G{% endequation %}. הענין הוא שבאמת קיים, הוכחנו את זה בשעתו, כשהוכחתי קיום של אידאל גנרי; ההוכחה הייתה "בואו נראה שלכל תנאי כפיה {% equation %}p\in P{% endequation %} קיים אידאל גנרי שמכיל אותו", והנה זה מסייע לנו עכשיו.

נשאר הכיוון השני, שבו אני מניח ש-{% equation %}\left(p,\tau_{1},\tau_{2}\right)\in\mathcal{F}_{\alpha}{% endequation %} ומוכיח ש-{% equation %}p{% endequation %} כופה את {% equation %}\tau_{1}=\tau_{2}{% endequation %}. את זה נעשה ישירות מההגדרה: ניקח אידאל גנרי {% equation %}G{% endequation %} כך ש-{% equation %}p\in G{% endequation %} ונוכיח {% equation %}\tau_{1}^{G}=\tau_{2}^{G}{% endequation %}. את זה נקבל מטענת העזר שטרם הוכחנו

<ul> <li>אם יש {% equation %}p\in G{% endequation %} שכל הרחבה שלו שייכת ל-{% equation %}A{% endequation %}, אז {% equation %}\tau_{1}^{G}\subseteq\tau_{2}^{G}{% endequation %}.</li>

</ul>

ותנאי ה"כל הרחבה שלו שייכת ל-{% equation %}A{% endequation %}" זה בדיוק מה שראינו קודם - האופן שבו התנאי שמגדיר את {% equation %}\mathcal{F}_{\alpha}{% endequation %} אומר "לכל הרחבה {% equation %}q_{1}{% endequation %} של {% equation %}p{% endequation %}, מתקיים ש-{% equation %}q_{1}\in A{% endequation %}". לכן {% equation %}\tau_{1}^{G}\subseteq\tau_{2}^{G}{% endequation %} ובאותו אופן גם {% equation %}\tau_{2}^{G}\subseteq\tau_{1}^{G}{% endequation %} וקיבלנו את {% equation %}\tau_{1}^{G}=\tau_{2}^{G}{% endequation %} כפי שרצינו. זה משלים את המשפט, למעט טענות העזר.

<h2>טענות העזר</h2>

כמעט סיימנו! רק נותרו לנו טענות העזר שהתבססנו עליהן שוב ושוב. שתיהן כזכור נגעו לקבוצה {% equation %}A{% endequation %} כלשהי. אז הנה התזכורת:

<ul> <li>הגדרת {% equation %}A{% endequation %}: {% equation %}q_{1}\in A{% endequation %} אם לכל {% equation %}\sigma_{1}{% endequation %} כך ש-{% equation %}\left(\sigma_{1},q_{1}\right)\in\tau_{1}{% endequation %} קיים {% equation %}\left(\sigma_{2},\tau_{2}\right)\in\tau_{2}{% endequation %} כך ש-{% equation %}q_{1}\subseteq q_{2}{% endequation %} ו-{% equation %}q_{2}{% endequation %} כופה את {% equation %}\sigma_{1}=\sigma_{2}{% endequation %}. </li>


<li>טענה 1: אם {% equation %}\tau_{1}^{G}\subseteq\tau_{2}^{G}{% endequation %} אז {% equation %}G\subseteq A{% endequation %}.</li>


<li>טענה 2: אם יש {% equation %}p\in G{% endequation %} שכל הרחבה שלו שייכת ל-{% equation %}A{% endequation %}, אז {% equation %}\tau_{1}^{G}\subseteq\tau_{2}^{G}{% endequation %}.</li>

</ul>

נתחיל מטענה 1. נניח ש-{% equation %}\tau_{1}^{G}\subseteq\tau_{2}^{G}{% endequation %} וניקח {% equation %}q_{1}\in G{% endequation %} כלשהו. אנחנו רוצים להראות ש-{% equation %}q_{1}\in A{% endequation %}. אז יהא {% equation %}\sigma_{1}{% endequation %} כלשהו כך שמתקיים {% equation %}\left(\sigma_{1},q_{1}\right)\in\tau_{1}{% endequation %}: המטרה שלנו היא למצוא {% equation %}\left(\sigma_{2},\tau_{2}\right)\in\tau_{2}{% endequation %} כך ש-{% equation %}q_{2}{% endequation %} שמרחיב את {% equation %}q_{1}{% endequation %} וכופה את {% equation %}\sigma_{1}=\sigma_{2}{% endequation %}.

מכיוון ש-{% equation %}\left(\sigma_{1},q_{1}\right)\in\tau_{1}{% endequation %} אז {% equation %}\sigma_{1}^{G}\in\tau_{1}^{G}{% endequation %} (זוכרים? האיברים של {% equation %}\tau_{1}^{G}{% endequation %} הם בדיוק שמות ה-{% equation %}P{% endequation %} שעוברים את הפילטר של {% equation %}G{% endequation %} ואז אנחנו רקורסיבית מחשבים את הערך ש-{% equation %}G{% endequation %} נותן להם) ולכן {% equation %}\sigma_{1}^{G}\in\tau_{2}^{G}{% endequation %}. זה אומר שבין שמות ה-{% equation %}P{% endequation %} שמרכיבים את {% equation %}\tau_{2}{% endequation %} חייב להיות אחד שהערך ש-{% equation %}G{% endequation %} נותן לו הוא {% equation %}\sigma_{1}^{G}{% endequation %}; במילים אחרות, יש {% equation %}\left(\sigma_{2},q_{2}\right)\in\tau_{2}{% endequation %} כך ש-{% equation %}q_{2}\in G{% endequation %} וגם {% equation %}\sigma_{2}^{G}=\sigma_{1}^{G}{% endequation %}.

עכשיו, מכיוון ש-{% equation %}q_{1},q_{2}\in G{% endequation %} יש להם הרחבה משותפת {% equation %}q{% endequation %}, וכזכור (?) דרישה שלנו משמות-{% equation %}P{% endequation %} הייתה שאם {% equation %}\left(\sigma_{2},q_{2}\right)\in\tau_{2}{% endequation %} ו-{% equation %}q{% endequation %} מרחיב את {% equation %}q_{2}{% endequation %} אז גם {% equation %}\left(\sigma_{2},q\right)\in\tau_{2}{% endequation %}. זה מאפשר לנו להניח בלי הגבלת הכלליות ש-{% equation %}q_{1}\subseteq q_{2}{% endequation %} (אחרת נחליף את {% equation %}q_{2}{% endequation %} בהרחבה משותפת שלו ושל {% equation %}q_{1}{% endequation %}).

צריך לזכור שאנחנו עדיין בהקשר של הוכחת המשפט המרכזי באינדוקציה. מה שאומר שאפשר להיעזר בהנחת האינדוקציה:

<ul> <li>אידאל גנרי {% equation %}G{% endequation %} של {% equation %}P{% endequation %} מקיים {% equation %}\sigma_{1}^{G}=\sigma_{2}^{G}{% endequation %} אם ורק אם קיים {% equation %}p\in G{% endequation %} שכופה את {% equation %}\sigma_{1}=\sigma_{2}{% endequation %}.</li>

</ul>

כאשר הנחת האינדוקציה הזו מופעלת לא על {% equation %}\tau_{1},\tau_{2}{% endequation %} (האובייקטים עליהם אנחנו מנסים עכשיו להוכיח משהו) אלא על מי שבאים לפניהם בהיררכייה, כלומר שייכים אליהם, כלומר בפרט {% equation %}\sigma_{1},\sigma_{2}{% endequation %}; לכן ניסחתי את ההנחה באמצעותם.

מה מצאנו? ראינו כבר ש-{% equation %}\sigma_{2}^{G}=\sigma_{1}^{G}{% endequation %} ולכן קיים {% equation %}p\in G{% endequation %} שכופה את {% equation %}\sigma_{1}=\sigma_{2}{% endequation %}. אנחנו יכולים לקחת הרחבה משותפת של {% equation %}p{% endequation %} ושל {% equation %}q_{2}{% endequation %} וגם ההרחבה המשותפת הזו תכפה את {% equation %}\sigma_{1}=\sigma_{2}{% endequation %} מנימוק שכבר ראינו קודם: כל אידאל שמכיל את ההרחבה המשותפת הזו יכיל גם את {% equation %}p{% endequation %} עצמו, ולכן {% equation %}p{% endequation %} יכפה את השוויון באותו אידאל. זה מסיים את ההוכחה של טענה 1.

נשארה רק טענה 2: ניקח {% equation %}p\in G{% endequation %} שכל הרחבה שלו שייכת ל-{% equation %}A{% endequation %}, ונראה ש-{% equation %}\tau_{1}^{G}\subseteq\tau_{2}^{G}{% endequation %}. בשביל להראות את ההכלה, ניקח איבר כלשהו ב-{% equation %}\tau_{1}^{G}{% endequation %}; הצורה שלו היא {% equation %}\sigma_{1}^{G}{% endequation %} כאשר {% equation %}\left(\sigma_{1},q_{1}\right)\in\tau_{1}{% endequation %} עבור {% equation %}q_{1}{% endequation %} כלשהו. אפשר להניח ש-{% equation %}p\subseteq q_{1}{% endequation %} אחרת נחליף את {% equation %}q_{1}{% endequation %} בהרחבה המשותפת שלו ושל {% equation %}p{% endequation %}. בסיטואציה הזו, <strong>כל</strong> הרחבה {% equation %}q_{1}^{\prime}{% endequation %} של {% equation %}q_{1}{% endequation %} שייכת ל-{% equation %}A{% endequation %}. עכשיו, בואו נסמן ב-{% equation %}D{% endequation %} את קבוצת כל ה-{% equation %}q_{2}{% endequation %}-ים שכופים את {% equation %}\sigma_{1}=\sigma_{2}{% endequation %} עבור {% equation %}\sigma_{2}{% endequation %} כלשהו שמקיים {% equation %}\left(\sigma_{2},q_{2}\right)\in\tau_{2}{% endequation %}. פורמלית

{% equation %}D=\left\{ q_{2}\in P\ |\ \exists\left(\sigma_{2},q_{2}\right)\in\tau_{2}:q_{2}\Vdash\sigma_{1}=\sigma_{2}\right\} {% endequation %}

כמו קודם, ההגדרה הזו מראה ש-{% equation %}D\in\mathcal{M}{% endequation %} כי אפשר לנסח אותה במסגרת {% equation %}\mathcal{M}{% endequation %} באמצעות אקסיומת ההפרדה, תוך שימוש בהנחת האינדוקציה שמאפשרת לנו לנסח את {% equation %}q_{2}\Vdash\sigma_{1}=\sigma_{2}{% endequation %} בלשון של שייכות ל-{% equation %}\mathcal{F}_{\beta}{% endequation %}.

עכשיו, על פי ההגדרה של {% equation %}A{% endequation %} והעובדה שכל הרחבה של {% equation %}q_{1}{% endequation %} שייכת ל-{% equation %}A{% endequation %}, קיבלנו שלכל הרחבה של {% equation %}q_{1}{% endequation %} קיימת הרחבה ב-{% equation %}D{% endequation %}. זה מתקשר להגדרה שהצגתי קודם:

<ul> <li>אני אומר על קבוצה {% equation %}D\in\mathcal{M}{% endequation %} שהיא <strong>צפופה מעל</strong> {% equation %}p{% endequation %} כלשהו אם לכל הרחבה של {% equation %}p{% endequation %} קיימת הרחבה ב-{% equation %}D{% endequation %}</li>

</ul>

כלומר {% equation %}D{% endequation %} צפופה מעל {% equation %}q_{1}{% endequation %}, בהינתן שאוכיח ש-{% equation %}D\in\mathcal{M}{% endequation %}. זה טוב לנו כי קודם הראיתי את טענת העזר

<ul> <li>אם {% equation %}G{% endequation %} הוא אידאל גנרי ו-{% equation %}D{% endequation %} צפופה מעל {% equation %}p\in G{% endequation %} כלשהו, אז {% equation %}G\cap D\ne\emptyset{% endequation %}</li>

</ul>

מה שמסיים את ההוכחה כי אז ה-{% equation %}p\in G\cap D{% endequation %} הזה כופה את {% equation %}\sigma_{1}^{G}=\sigma_{2}^{G}{% endequation %}. זה אומר שלקחנו איבר כללי {% equation %}\sigma_{1}^{G}\in\tau_{1}^{G}{% endequation %} והראינו שהוא שייך ל-{% equation %}\tau_{2}^{G}{% endequation %}, מה שמוכיח את {% equation %}\tau_{1}^{G}\subseteq\tau_{2}^{G}{% endequation %} המבוקש. זה מסיים את כל מה שנשאר לנו מההוכחה!

<h2>סיכום ביניים לפני שממשיכים הלאה</h2>

מה הלך בפוסט הזה? אפשר לסכם אותו בשלוש נקודות עיקריות:

<ul> <li>ראינו את מושג ה<strong>כפייה</strong>: {% equation %}p\Vdash\phi\left(\tau_{1},\ldots,\tau_{n}\right){% endequation %} ({% equation %}p{% endequation %} כופה את {% equation %}\phi\left(\tau_{1},\ldots,\tau_{n}\right){% endequation %}) אם <strong>לכל</strong> אידאל גנרי {% equation %}G{% endequation %} כך ש-{% equation %}p\in G{% endequation %}, מתקיים ש-{% equation %}\mathcal{M}\left[G\right]\models\phi\left(\tau_{1}^{G},\ldots,\tau_{n}^{G}\right){% endequation %}</li>


<li>ראינו את המשפט היסודי של תורת הכפייה: לכל אידאל גנרי {% equation %}G{% endequation %}, נוסחה {% equation %}\phi\left(x_{1},\ldots,x_{n}\right){% endequation %} ושמות-{% equation %}P{% endequation %} {% equation %}\tau_{1},\ldots,\tau_{n}{% endequation %}, מתקיים ש-{% equation %}\mathcal{M}\left[G\right]\models\phi\left(\tau_{1}^{G},\ldots,\tau_{n}^{G}\right){% endequation %} אם ורק אם קיים {% equation %}p\in G{% endequation %} כך ש-{% equation %}p{% endequation %} כופה את {% equation %}\phi\left(\tau_{1},\ldots,\tau_{n}\right){% endequation %}.</li>


<li><strong>הוכחנו</strong> את המשפט היסודי למקרה הפרטי של הנוסחה {% equation %}\phi\left(x_{1},x_{2}\right){% endequation %} שמתארת שוויון, {% equation %}x_{1}=x_{2}{% endequation %}.</li>

</ul>

ההוכחה של המקרה הפרטי הייתה ארוכה, מסובכת ועם שלל טענות עזר ושימושים בהגדרות שראינו עד כה - כל מה שעשינו עד עכשיו התרכז לנקודה הזו, בעצם. למרות שאין פה משהו קשה באמת קל מאוד ללכת לאיבוד בפרטים; עבורי כתיבת הפוסט הזה הייתה הפעם הראשונה שבה הצלחתי (אני מקווה...) לעקוב לגמרי אחרי כל המעברים, אז ממש לא קריטי אם הולכים לאיבוד.

מה נשאר לנו?

<ul> <li>להוכיח את המשפט למקרה הכללי: זה יהיה <strong>יותר קל</strong> מאשר מה שקרה עד כה, אינטואיטיבית בגלל שכאן "התחלנו מאפס" ובהמשך נוכל להסתמך על מה שהוכחנו כאן.</li>


<li>להראות איך המשפט מוכיח לנו שההרחבה הגנרית {% equation %}\mathcal{M}\left[G\right]{% endequation %} (זוכרים שהיה פעם משהו כזה?) מקיימת את כל אקסיומות ZFC.</li>


<li>להשתמש בתוצאות הללו כדי להראות איך בונים {% equation %}\mathcal{M}\left[G\right]{% endequation %} אחד שבו השערת הרצף <strong>מתקיימת</strong> ו-{% equation %}\mathcal{M}\left[G\right]{% endequation %} אחר שבו השערת הרצף <strong>לא מתקיימת</strong>.</li>

</ul>

כל אלו עדיין ידרשו עבודה, אבל עבודה פחות טכנית ועם יותר הבנה של התמונה הגדולה. אז קדימה לדרך! 