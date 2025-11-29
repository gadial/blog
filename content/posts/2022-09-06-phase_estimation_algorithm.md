---
title: "חישוב קוונטי: אלגוריתם הערכת פאזה"
layout: post
categories:
  - חישוב קוונטי
tags:
  - חישוב קוונטי
description: "התמרת פורייה הקוונטית הייתה קסם, והערכת פאזה מתבססת עליה כדי לעשות קסם בריבוע"
image: "2022/phase_estimation.png"


---


<h2>מה זה בכלל ובשביל מה זה טוב?</h2>

האלגוריתם הקוונטי שאני רוצה להציג בפוסט הזה, <strong>אלגוריתם הערכת פאזה</strong>, הוא פשוט קסם. מה שהוא עושה הוא קסם. האופן שבו הוא עושה את זה הוא קסם. האופן שבו זה משתלב עם התמרת פורייה הקוונטית שעליה <a href="https://gadial.net/2022/09/01/quantum_fourier_transform/">דיברתי בפוסט הקודם</a> הוא קסם. הדבר היחיד שאינו קסם, חוץ מההוכחה הפורמלית שהכל עובד והיא טכנית למדי, הוא להבין בשביל מה זה טוב. אז אני אשתמש באותו תירוץ שהשתמשתי בו בפוסט על התמרת פורייה הקוונטית - זה הכלי המרכזי שבו משתמש האלגוריתם של שור לפירוק לגורמים. למעשה, אפשר לחשוב על כל החלק הקוונטי באלגוריתם של שור בתור מקרה פרטי של אלגוריתם הערכת פאזה. אבל בשביל זה באמת צריך להסביר מה זה האלגוריתם הזה ומה הוא עושה.

הרעיון בהערכת פאזה הוא זה: נניח שיש לנו מרחב על {% equation %}m{% endequation %} קיוביטים, כלומר {% equation %}\mathbb{C}^{2^{m}}{% endequation %}, ועל המרחב הזה מוגדר לנו אופרטור אוניטרי {% equation %}U:\mathbb{C}^{2^{m}}\to\mathbb{C}^{2^{m}}{% endequation %}, ואני מניח שלאופרטור הזה יש וקטור עצמי, {% equation %}\left|u\right\rangle {% endequation %}. עכשיו, הערכים העצמיים של אופרטורים אוניטריים הם תמיד מנורמה 1, אז אפשר לכתוב את הערך העצמי שמתאים ל-{% equation %}\left|u\right\rangle {% endequation %} בתור {% equation %}e^{2i\pi\cdot\varphi}{% endequation %}, כאשר המספר {% equation %}\varphi{% endequation %} נקרא <strong>הפאזה</strong> של הערך העצמי. המטרה שלנו היא לחשב את {% equation %}\varphi{% endequation %}, עד רמת דיוק מסויימת שנוכל לשלוט עליה ולהגדיל אותה כרצוננו; אבל מכיוון שתמיד נקבל מספר רציונלי ו-{% equation %}\varphi{% endequation %} עשוי להיות אי רציונלי, גם ברמת דיוק גבוהה עדיין ייתכן שנקבל רק <strong>הערכה</strong> של הערך של {% equation %}\varphi{% endequation %}, ומכאן שם האלגוריתם.

זה אלגוריתם מעניין למדי כבר בשלב הזה, כי הוא עושה משהו שלא ראינו עד כה - מחשב ערך מספרי כלשהו ומחזיר אותו לנו. לא לגמרי ברור איך עושים את זה, או למה זה חשוב; עד סוף הפוסט אני מקווה שחלק מהערפל הזה קצת יתבהר, אבל לשימושים לא נגיע הפעם.

<h2>אלגוריתם הערכת פאזה, תיאור פורמלי וקסום</h2>

אבני הבניין שמהן אנו בונים את אלגוריתם הערכת הפאזה הן שלוש: קודם כל, אנו נעזרים ב-{% equation %}n{% endequation %} קיוביטים שמאותחלים ל-{% equation %}\left|0^{n}\right\rangle {% endequation %}, כאשר {% equation %}n{% endequation %} מתאר את רמת הדיוק שלנו - אנחנו הולכים לקבל כפלט מספר בן {% equation %}n{% endequation %} ספרות בינאריות אחרי הנקודה שהוא קירוב של {% equation %}\varphi{% endequation %} (ואם {% equation %}\varphi{% endequation %} עצמו ניתן לתיאור מדויק באמצעות {% equation %}n{% endequation %} ספרות בינאריות אחרי הנקודה, נקבל אותו במדויק). שנית, אנו נעזרים ב-{% equation %}t{% endequation %} קיוביטים נוספים שהמצב שלהם בתחילת האלגוריתם הוא {% equation %}\left|u\right\rangle {% endequation %}, הוקטור העצמי שאת הפאזה שלו מחפשים (בפוסט על האלגוריתם של שור נראה שלא באמת <strong>חייבים</strong> לדעת את {% equation %}\left|u\right\rangle {% endequation %}). לבסוף, אנחנו מניחים שיש לנו יכולת לבנות מעגל שמחשב את {% equation %}U{% endequation %}, אבל יותר מזה - גם את {% equation %}U^{2},U^{4},U^{8},\ldots{% endequation %} וכדומה, עבור חזקות {% equation %}U^{2^{t}}{% endequation %} עם {% equation %}t\ge0{% endequation %}. למה רק חזקות של 2? כי נראה שהן יספיקו לנו כדי לחשב את כל החזקות של {% equation %}U{% endequation %} שנזדקק להן.

בהינתן שיש לנו את כל אלו (וזו לא הנחה טריוויאלית), אלגוריתם הערכת הפאזה די קל לתיאור קונספטואלי. אני אקרא לקיוביטים שאותחלו ל-{% equation %}\left|0^{n}\right\rangle {% endequation %} בשם "הרגיסטר הראשון" ולקיוביטים שמהווים את {% equation %}\left|u\right\rangle {% endequation %} בשם "הרגיסטר השני", וכעת מה שעושים הוא:

<ul> <li>מפעילים {% equation %}H{% endequation %} על כל אברי הרגיסטר הראשון.</li>


<li>מפעילים את הטרנספורמציה {% equation %}\left|k\right\rangle \left|u\right\rangle \mapsto\left|k\right\rangle U^{k}\left|u\right\rangle {% endequation %} על שני הרגיסטרים.</li>


<li>מפעילים את {% equation %}\text{QFT}_{N}^{\dagger}{% endequation %} על הרגיסטר הראשון.</li>


<li>מודדים את הרגיסטר הראשון. תוצאת המדידה תהיה הקירוב המבוקש.</li>

</ul>

בתור מין מעגל סכמטי, זה נראה כך:

<img src="{{site.baseurl}}{{site.post_images}}/2022/phase_estimation_overview.png" alt=""/>

אבל כרגע רב הנסתר על המרובה. להפעיל {% equation %}H{% endequation %} על אברי הרגיסטר הראשון - את זה אנחנו כבר מבינים, וגם יודעים שזה מייצר לנו את המצב {% equation %}\left|+^{n}\right\rangle {% endequation %}. אבל איך מבצעים את הטרנספורמציה {% equation %}\left|k\right\rangle \left|u\right\rangle \mapsto\left|k\right\rangle U^{k}\left|u\right\rangle {% endequation %} ומה זה {% equation %}\text{QFT}_{N}^{\dagger}{% endequation %}? נתחיל מהשני. בפוסט הקודם על התמרת פורייה תיארנו מעגל שמחשב את {% equation %}\text{QFT}_{N}{% endequation %}. הסימון {% equation %}\text{QFT}_{N}^{\dagger}{% endequation %} פשוט מייצג את הטרנספורמציה <strong>ההופכית</strong>. קל לחשב אותה, כי חישוב קוונטי שלא מערב מדידות הוא <strong>הפיך</strong> - פשוט לוקחים את המעגל של {% equation %}\text{QFT}_{N}{% endequation %} ושמים את כל השערים שלו בסדר הפוך. פורמלית, מה שמשתמשים בו בהערכת פאזה הוא לא "התמרת פורייה הקוונטית" אלא "התמרת פורייה הקוונטית ההפוכה", ועוד מעט ייפול לנו גם האסימון למה.

השאלה השניה היא איך מחשבים את {% equation %}\left|k\right\rangle \left|u\right\rangle \mapsto\left|k\right\rangle U^{k}\left|u\right\rangle {% endequation %}, וכאן זה הולך להיות דומה <strong>מאוד</strong> למה שקרה בהתמרת פורייה הקוונטית. כל כך דומה, שאני ממליץ בחום לחזור ולקרוא את הפוסט ההוא למי שדילגו עליו (מצד שני, אולי זה פשוט יותר כאן, ויקל על מי שנתקעו בפוסט ההוא?)

כזכור, אנחנו אוהבים ייצוג <strong>בינארי</strong> של מספרים. הייצוג הבינארי של מספר {% equation %}k{% endequation %} הוא ייצוג בתור {% equation %}k=\sum_{t=1}^{n}2^{n-t}k_{t}{% endequation %} כך ש-{% equation %}k_{t}\in\left\{ 0,1\right\} {% endequation %}. עכשיו, אפשר לפרק העלאה כללית בחזקת {% equation %}k{% endequation %} למכפלה של העלאות בחזקות של 2:

{% equation %}U^{k}=U^{\sum_{t=1}^{n}2^{n-t}k_{t}}=\prod_{t=1}^{n}U^{2^{n-t}k_{t}}=\prod_{k_{t}=1}U^{2^{n-t}}{% endequation %}

אז האפקט שאנחנו רוצים הוא בעצם:

{% equation %}\left|k_{1}k_{2}\ldots k_{n}\right\rangle \left|u\right\rangle \mapsto\left|k_{1}k_{2}\ldots k_{n}\right\rangle \prod_{k_{t}=1}U^{2^{n-t}}\left|u\right\rangle {% endequation %}

ראינו משהו דומה לזה בפוסט על פורייה, ושם הטריק שלנו היה שאפשר לעבור מסכום של {% equation %}2^{n}{% endequation %} איברים שכל אחד מהם הוא מכפלה של {% equation %}n{% endequation %} קיוביטים (כלומר, הסכום הוא על כל המכפלות האפשריות) אל מכפלה טנזורית של {% equation %}n{% endequation %} הקיוביטים שכל אחד מהם הוא בסופרפוזיציה של בדיוק שני מצבים. אני ארצה לעשות את זה גם כאן, אבל בגלל שמעורבים פה שני רגיסטרים קוונטיים שונים, אחד עם {% equation %}\left|k_{1}k_{2}\ldots k_{n}\right\rangle {% endequation %} ואחד עם {% equation %}\left|u\right\rangle {% endequation %}, זה יותר מסובך - אני צריך להוציא החוצה את {% equation %}\left|u\right\rangle {% endequation %} איכשהו, וקל לי לעשות את זה כי {% equation %}\left|u\right\rangle {% endequation %} הוא <strong>וקטור עצמי</strong> של {% equation %}U{% endequation %} ולכן הפעולה של {% equation %}U{% endequation %} עליו מתורגמת לכפל בסקלר, ואת הסקלר אני יכול להעביר אל {% equation %}\left|k_{1}k_{2}\ldots k_{n}\right\rangle {% endequation %}:

{% equation %}\left|k_{1}k_{2}\ldots k_{n}\right\rangle \prod_{k_{t}=1}U^{2^{n-t}}\left|u\right\rangle =\left|k_{1}k_{2}\ldots k_{n}\right\rangle \prod_{k_{t}=1}e^{2\pi i\varphi\cdot2^{n-t}}\left|u\right\rangle ={% endequation %}

{% equation %}\prod_{k_{t}=1}e^{2\pi i\varphi\cdot2^{n-t}}\left|k_{1}k_{2}\ldots k_{n}\right\rangle \left|u\right\rangle {% endequation %}

עכשיו בואו נעשה טריק כמו בפורייה: ראשית ניקח סכום של כל {% equation %}2^{n}{% endequation %} מצבי הבסיס {% equation %}\left|k_{1}k_{2}\ldots k_{n}\right\rangle {% endequation %}. הוא יצטרך להיות משוקלל, כלומר נחלק אותו ב-{% equation %}\frac{1}{2^{n/2}}{% endequation %}. נקבל שצריך להגיע אל

{% equation %}\frac{1}{2^{n/2}}\sum_{k=0}^{2^{n}-1}\prod_{k_{t}=1}e^{2\pi i\varphi\cdot2^{n-t}}\left|k_{1}k_{2}\ldots k_{n}\right\rangle \left|u\right\rangle ={% endequation %}

{% equation %}=\frac{1}{2^{n/2}}\bigotimes_{t=1}^{n}\left(\left|0\right\rangle +e^{2\pi i\varphi\cdot2^{n-t}}\left|1\right\rangle \right)\left|u\right\rangle {% endequation %}

{% equation %}=\bigotimes_{t=1}^{n}\left(\frac{\left|0\right\rangle +e^{2\pi i\varphi\cdot2^{n-t}}\left|1\right\rangle }{\sqrt{2}}\right)\left|u\right\rangle {% endequation %}

מה שאנחנו רואים פה הוא שאפשר לחשוב על היעד שלנו בתור משהו שבו {% equation %}\left|u\right\rangle {% endequation %} המקורי לא השתנה, אבל ברגיסטר הראשון הקיוביט ה-{% equation %}t{% endequation %} התחלף מ-{% equation %}\left|0\right\rangle {% endequation %} תמים אל {% equation %}\frac{\left|0\right\rangle +e^{2\pi i\varphi\cdot2^{n-t}}\left|1\right\rangle }{\sqrt{2}}{% endequation %}. איך משיגים אפקט כזה? ראשית, כמו שאמרתי כבר, מפעילים {% equation %}H{% endequation %} בהתחלה על כל הקיוביטים ברגיסטר הזה - זה מעביר כל אחד מהם אל {% equation %}\frac{\left|0\right\rangle +\left|1\right\rangle }{\sqrt{2}}{% endequation %}. עכשיו רק צריך להכניס את הפאזה {% equation %}e^{2\pi i\varphi\cdot2^{n-t}}{% endequation %} לתוך המקדם של {% equation %}\left|1\right\rangle {% endequation %} מבלי לגעת ב-{% equation %}\left|0\right\rangle {% endequation %}. את זה אפשר לעשות עם שער <strong>מותנה</strong>. מה שאני רוצה שיקרה הוא

<ul> <li>{% equation %}\left|0\right\rangle \left|u\right\rangle \mapsto\left|0\right\rangle \left|u\right\rangle {% endequation %}</li>


<li>{% equation %}\left|1\right\rangle \left|u\right\rangle \mapsto\left|1\right\rangle U^{2^{n-t}}\left|u\right\rangle =e^{2\pi i\varphi\cdot2^{n-t}}\left|1\right\rangle \left|u\right\rangle {% endequation %}</li>

</ul>

אז אני הולך להפעיל שער {% equation %}U^{2^{n-t}}{% endequation %} שמותנה בקיוביט ה-{% equation %}t{% endequation %}-י. ככה זה הולך להיראות:

<img src="{{site.baseurl}}{{site.post_images}}/2022/phase_estimation.png" alt=""/>

אפשר כמובן לשאול איך בונים שערי {% equation %}U^{2^{t}}{% endequation %} מותנים בפועל - זו שאלה שאלגוריתם הערכת הפאזה עצמו לא מתעסק בה; הוא אומר "אם {% equation %}U{% endequation %} הוא נחמד ואתם יכולים לבנות את השערים הללו עבורו, אז אפשר להפעיל הערכת פאזה" אבל בשימוש ספציפי, כמו אלגוריתם שור, אכן נצטרך להסביר איך לעשות את זה.

שימו לב שעל פניו, קורה כאן משהו מוזר <strong>מאוד</strong>: אחרי שערי ה-{% equation %}H{% endequation %} בהתחלה, לכאורה על שערי הרגיסטר הראשון לא מופעל שום דבר שמשנה אותם - רק שערים שמותנים בהם. והרגיסטר השני? מופעלים עליו {% equation %}U^{j}{% endequation %}-ים, אבל בגלל ש-{% equation %}\left|u\right\rangle {% endequation %} הוא וקטור עצמי של {% equation %}U{% endequation %} זה לא משנה את {% equation %}\left|u\right\rangle {% endequation %} - רק מכפיל אותו בסקלר כלשהו, ואחר כך אנחנו בכל מקרה לא מודדים את {% equation %}\left|u\right\rangle {% endequation %} אז לכאורה הסקלר אמור "להיעלם". מה הולך כאן? זה נראה כמו קסם - מעגל שלא עושה כלום ומחשב בדיוק את מה שהוא אמור.

כמובן שאין פה קסם - הסקלר של {% equation %}\left|u\right\rangle {% endequation %} לא הולך להיעלם אלא להצטבר בצורה חכמה בתוך הסופרפוזיציה שמהווים אברי הרגיסטר הראשון. איך זה ייתכן, אם אנחנו לא פועלים עליהם? ובכן, אין דבר כזה בחישוב קוונטי, לומר בנחרצות כזו שאנחנו לא פועלים על משהו; שערים מותנים הם לא משהו שפועל על כל קיוביט בנפרד אלא על זוג קיוביטים ביחד, וצריך לחשוב על ההשפעה שלהם בתור משהו שמשפיע על שני הקיוביטים הללו יחד. כבר ראינו איך זה בא לידי ביטוי פורמלי.

עכשיו אנחנו קרובים בצורה מפתיעה לסיום ההבנה של "למה זה עובד". נשאר רק דבר אחד, בעצם. בואו נסתכל על מצב הרגיסטר הראשון אחרי סיום ריצת המעגל:

{% equation %}\bigotimes_{t=1}^{n}\frac{1}{\sqrt{2}}\left(\left|0\right\rangle +e^{2\pi i\varphi\cdot2^{n-t}}\left|1\right\rangle \right){% endequation %}

ובוא נזכיר לעצמנו מה עשתה התמרת פורייה הקוונטית, בפוסט הקודם:

{% equation %}\text{QFT}_{N}\left(\left|j\right\rangle \right)=\bigotimes_{t=1}^{n}\frac{1}{\sqrt{2}}\left(\left|0\right\rangle +e^{2\pi i0.j_{n-t+1}\ldots j_{n}}\left|1\right\rangle \right){% endequation %}

הדמיון בין שני הביטויים עצום, והוא יגדל עוד יותר אם נזכיר לעצמנו מה בעצם הולך בביטוי {% equation %}\varphi\cdot2^{n-t}{% endequation %}. הפאזה {% equation %}\varphi{% endequation %} עצמה היא מספר בין 0 ל-1, כלומר אפשר לכתוב {% equation %}\varphi=0.\varphi_{1}\varphi_{2}\ldots{% endequation %} בייצוג בינארי. עכשיו, לכפול את זה ב-{% equation %}2^{n-t}{% endequation %} פירושו "להזיז שמאלה" את הספרות {% equation %}n-t{% endequation %} צעדים, ומכיוון שכל זה קורה במעריך של {% equation %}e^{2\pi i}{% endequation %}, הספרות שמשמאל לנקודה הבינארית פשוט ייעלמו (זה היה הטריק המרכזי שלנו בהתמרת פורייה הקוונטית). אז מה שבעצם הגענו אליו הוא

{% equation %}\bigotimes_{t=1}^{n}\frac{1}{\sqrt{2}}\left(\left|0\right\rangle +e^{2\pi i0.\varphi_{n-t+1}\ldots\varphi_{n}\ldots}\left|1\right\rangle \right){% endequation %}

עכשיו, אם {% equation %}\varphi=0.\varphi_{1}\varphi_{2}\ldots\varphi_{n}{% endequation %} הוא ייצוג <strong>מדויק</strong> של {% equation %}\varphi{% endequation %} באמצעות {% equation %}n{% endequation %} ספרות בינאריות, אז מה שקיבלנו הוא <strong>בדיוק</strong>

{% equation %}\bigotimes_{t=1}^{n}\frac{1}{\sqrt{2}}\left(\left|0\right\rangle +e^{2\pi i0.\varphi_{n-t+1}\ldots\varphi_{n}}\left|1\right\rangle \right)=\text{QFT}_{N}\left(\left|\varphi_{1}\varphi_{2}\ldots\varphi_{n}\right\rangle \right){% endequation %}

ולכן, אם אחרי המעגל שכבר הראינו אנחנו מוסיפים {% equation %}\text{QFT}_{N}^{\dagger}{% endequation %}, נסיים במצב הקוונטי הבודד {% equation %}\left|\varphi_{1}\varphi_{2}\ldots\varphi_{n}\right\rangle {% endequation %}, וכשנמדוד אותו נקבל את סדרת הספרות {% equation %}\varphi_{1}\varphi_{2}\ldots\varphi_{n}{% endequation %} בהסתברות 1.

זה ממש קסם.

<h2>ועכשיו לחלק הפחות קסום</h2>

אם אפשר לייצג את הפאזה {% equation %}\varphi{% endequation %} בעזרת {% equation %}n{% endequation %} ספרות בינאריות, האלגוריתם עובד מושלם. אבל אם אי אפשר לייצג כך את הפאזה, הכל הופך ליותר מסובך וטכני. במקרה הזה בודאות לא נוכל לקבל את {% equation %}\varphi{% endequation %} במדויק ולכן בכל מקרה נקבל <strong>קירוב</strong> שלו; אנחנו רוצים להשתכנע שגם במקרה הזה, בהסתברות טובה נקבל קירוב <strong>טוב</strong>.

אני הולך להיכנס לפרטים הטכניים של הניתוח עד הסוף, אבל מי שמתייאשים באמצע לא חייבים לסבול; אפשר לקפוץ לתחילת החלק הבא שבו אסכם את כל מה שצריך לדעת.

בשביל הניתוח במקרה הזה, יהיה לנו יותר נוח לחשוב על ייצוג המצב בתור סכום של {% equation %}N=2^{n}{% endequation %} מחוברים. אז בואו ניזכר מה קורה בשני השלבים הראשונים:

{% equation %}\left|0^{n}\right\rangle \left|u\right\rangle \mapsto\frac{1}{2^{n/2}}\sum_{k=0}^{2^{n}-1}\left|k\right\rangle \left|u\right\rangle \mapsto\frac{1}{2^{n/2}}\sum_{k=0}^{2^{n}-1}\left|k\right\rangle U^{k}\left|u\right\rangle ={% endequation %}

{% equation %}=\frac{1}{\sqrt{N}}\sum_{k=0}^{N-1}e^{2\pi i\varphi\cdot k}\left|k\right\rangle \left|u\right\rangle {% endequation %}

עכשיו, מה הפעלת {% equation %}\text{QFT}_{N}^{\dagger}{% endequation %} עושה? כזכור

{% equation %}\text{QFT}_{N}\left(\left|j\right\rangle \right)\frac{1}{\sqrt{N}}\sum_{j=0}^{N-1}e^{\frac{2\pi i}{N}jk}\left|k\right\rangle {% endequation %}

כדי לקבל את {% equation %}\text{QFT}_{N}^{\dagger}{% endequation %} אפשר פשוט להפעיל צמוד מרוכב על אגף ימין; הדבר היחיד שהוא עושה הוא להחליף את {% equation %}i{% endequation %} (המספר המרוכב {% equation %}i{% endequation %}; זה לא אינדקס) ב-{% equation %}-i{% endequation %}. אז בואו נכתוב את זה - ואני גם אחליף את הסימונים של מצבי הקלט והפלט, כך שהקלט יהיה דווקא {% equation %}k{% endequation %} והפלט דווקא {% equation %}j{% endequation %}, כי עדיין קונספטואלית אני הופך את הסדר, וזה גם מתאים לשימוש שתכף אבצע בזה:

{% equation %}\text{QFT}_{N}^{\dagger}\left(\left|k\right\rangle \right)\frac{1}{\sqrt{N}}\sum_{j=0}^{N-1}e^{-\frac{2\pi i}{N}jk}\left|j\right\rangle {% endequation %}

ולכן הפעלת {% equation %}\text{QFT}_{N}^{\dagger}{% endequation %} על המצב שהגענו אליו ברגיסטר הראשון תניב

{% equation %}\text{QFT}_{N}^{\dagger}\left(\frac{1}{\sqrt{N}}\sum_{k=0}^{N-1}e^{2\pi i\varphi\cdot k}\left|k\right\rangle \right)={% endequation %}

{% equation %}\frac{1}{\sqrt{N}}\sum_{k=0}^{N-1}e^{2\pi i\varphi\cdot k}\text{QFT}_{N}^{\dagger}\left(\left|k\right\rangle \right)={% endequation %}

{% equation %}=\frac{1}{N}\sum_{k=0}^{N-1}\sum_{j=0}^{N-1}e^{2\pi i\varphi\cdot k}e^{-2\pi i\cdot\frac{jk}{N}}\left|j\right\rangle ={% endequation %}

{% equation %}=\frac{1}{N}\sum_{j=0}^{N-1}\sum_{k=0}^{N-1}e^{2\pi i\left(\varphi-\frac{j}{N}\right)k}\left|j\right\rangle {% endequation %}

קיבלנו פה סופרפוזיציה של הרבה מצבים; כדי להבין מה ההסתברות שמדידה תעלה בגורל מצב {% equation %}\left|j\right\rangle {% endequation %} נסתכל על המקדם שלו, מה שאני מכנה <strong>האמפליטודה</strong> שלו ומסמן {% equation %}\alpha_{j}{% endequation %}; ההעלאה בריבוע של הערך המוחלט של האמפליטודה תיתן לנו את ההסתברות ש-{% equation %}\left|j\right\rangle {% endequation %} יעלה בגורל. באופן כללי האמפליטודה הזו תהיה

{% equation %}\alpha_{j}=\frac{1}{N}\sum_{k=0}^{N-1}e^{2\pi i\left(\varphi-\frac{j}{N}\right)k}{% endequation %}

האם אפשר לפשט את זה קצת? בהחלט, יש לנו פה טור הנדסי! אם נזכור את חוקי החזקות: {% equation %}e^{ab}=\left(e^{a}\right)^{b}{% endequation %} אפשר לראות שבעצם קיבלנו פה את הסכום

{% equation %}\alpha_{j}=\frac{1}{N}\sum_{k=0}^{N-1}\left[e^{2\pi i\left(\varphi-\frac{j}{N}\right)}\right]^{k}{% endequation %}

וזה טור הנדסי, כלומר ביטוי מהצורה {% equation %}\sum_{k=0}^{N-1}q^{k}{% endequation %} כאשר במקרה שלנו {% equation %}q=e^{2\pi i\left(\varphi-\frac{j}{N}\right)}{% endequation %}. עכשיות למרות שמדגדג לי, לא אחזור על האופן שבו מוצאים את הסכום של טור הנדסי - <a href="https://gadial.net/2019/05/30/arithmetic_and_geometric_series/">יש לי פוסט</a> על זה. פשוט צריך לזכור ש-

{% equation %}\sum_{k=0}^{N-1}q^{k}=\frac{q^{N}-1}{q-1}=\frac{1-q^{N}}{1-q}{% endequation %}

(עברתי לצורה השניה כי היא קצת יותר אינטואיטיבית במקרה כמו שלנו שבו {% equation %}\left|q\right|<1{% endequation %})

ולכן במקרה שלנו נקבל

{% equation %}\alpha_{j}=\frac{1}{N}\left(\frac{1-e^{2\pi i\left(\varphi-\frac{j}{N}\right)\cdot N}}{1-e^{2\pi i\left(\varphi-\frac{j}{N}\right)}}\right)=\frac{1}{N}\left(\frac{1-e^{2\pi i\left(N\varphi-j\right)}}{1-e^{2\pi i\left(\varphi-j/N\right)}}\right){% endequation %}

זו האמפליטודה עבור מצב {% equation %}j{% endequation %} כללי. בואו ניקח אחד ספציפי שטוב לנו במיוחד: ניקח מספר {% equation %}b{% endequation %} שנותן לנו את הקירוב הטוב ביותר ל-{% equation %}\varphi{% endequation %} מלמלטה שכולל {% equation %}n{% endequation %} ספרות בינאריות. כלומר, ניקח {% equation %}0\le b<N{% endequation %} שמקיים ש-{% equation %}\frac{b}{N}=0.b_{1}b_{2}\ldots b_{n}{% endequation %}, {% equation %}\frac{b}{N}\le\varphi{% endequation %} ו-{% equation %}\delta=\left|\varphi-\frac{b}{N}\right|=\varphi-\frac{b}{N}{% endequation %} הוא מינימלי ביחס לדרישות הללו.

אנחנו לא יודעים, כמובן, מהו {% equation %}\delta{% endequation %} אבל ברור ש-{% equation %}0\le\delta\le\frac{1}{N}{% endequation %} (כי אם {% equation %}\frac{1}{N}<\delta{% endequation %} אפשר להגדיל את {% equation %}b{% endequation %} ב-{% equation %}\frac{1}{N}=\frac{1}{2^{n}}{% endequation %} על ידי חיבור 1 לספרה הכי פחות משמעותית בו ולקבל קירוב טוב יותר מ-{% equation %}b{% endequation %}).

לא כל כך קל לחסום מלמטה את ההסתברות לקבל את {% equation %}b{% endequation %} או דברים שקרובים אליו, אז נעשה את ההפך - נחסום מלמעלה את ההסתברות לקבל דברים שרחוקים מ-{% equation %}b{% endequation %}. 

לשם כך בואו נכניס לתמונה עוד סימון. נזכור ש-{% equation %}0\le b<N{% endequation %}, ולכן אפשר לתאר אברים אחרים בתחום הזה בתור {% equation %}b+d\text{ mod }N{% endequation %} כאשר {% equation %}d\in\mathbb{Z}{% endequation %} הוא מספר שלם כלשהו. למשל, אם {% equation %}N=8{% endequation %} ו-{% equation %}b=5{% endequation %} אז {% equation %}b+4=1{% endequation %} ו-{% equation %}b+\left(-7\right)=6{% endequation %} וכדומה. אני אשתמש ב-{% equation %}\beta_{d}{% endequation %} כדי לסמן את האמפליטודה של איבר שמיוצג כך, כלומר

{% equation %}\beta_{d}=\alpha_{b+d\left(\text{mod }N\right)}{% endequation %}

עכשיו השאלה היא כזו: נניח ש-{% equation %}e{% endequation %} הוא מספר חיובי כלשהו שבא לציין את "סף הרגישות לשגיאה" שלנו - ככל שהוא קטן יותר כך גודל השגיאות שאנחנו מוכנים לסבול הוא קטן יותר. פורמלית, אם {% equation %}m{% endequation %} הוא התוצאה שהאלגוריתם החזיר לנו, אנחנו מתחילים לכעוס אם {% equation %}\left|m-b\right|>e{% endequation %} (שימו לב ש-{% equation %}\left|m-b\right|{% endequation %} הוא <strong>לא</strong> כמה שאנחנו רחוקים מ-{% equation %}\varphi{% endequation %}; לניתוח של זה נגיע בהמשך). 

אם כן, מה ההסתברות שלנו לקבל במדידה {% equation %}m{% endequation %} בעייתי שכזה? בשביל זה אפשר להסתכל על כל ה-{% equation %}\beta_{d}{% endequation %}-ים כך ש-{% equation %}d\notin\left[-e,e\right]{% endequation %}, כל עוד אני לא לוקח {% equation %}d{% endequation %} גדול או קטן מדי עד שהוא כבר עושה סיבוב מסביב ל-{% equation %}N{% endequation %} וחוזר שוב לתחום {% equation %}\left[-e,e\right]{% endequation %}. לצורך זה אני אקח את כל ה-{% equation %}d{% endequation %}-ים שמקיימים או {% equation %}e+1\le d\le\frac{N}{2}{% endequation %} או {% equation %}-\frac{N}{2}<d\le-\left(e+1\right){% endequation %}. זה יבטיח שאני תופס את כל האיברים ה"בעייתיים" ולא לוקח איברים לא בעייתים, אלא אולי במקרי קיצון מוזרים וגם בהם הטעות הזו יכולה רק להיות לרעתנו (כי היא תנפח את ההסתברות לקבל משהו לא טוב) אבל הניתוח שלנו יצליח בכל מקרה.

אם כן, פורמלית:

{% equation %}p\left(\left|m-b\right|>e\right)\le\sum_{-N/2<d<-e}\left|\beta_{d}\right|^{2}+\sum_{e<d\le N/2}\left|\beta_{d}\right|^{2}{% endequation %}

כדי לעשות משהו מועיל עם הביטוי הזה אני צריך למצוא חסם מלמעלה על {% equation %}\left|\beta_{d}\right|^{2}{% endequation %}, כלומר חסם מלמעלה על {% equation %}\left|\beta_{d}\right|{% endequation %}, כלומר חסם מלמעלה על

{% equation %}\left|\beta_{d}\right|=\frac{1}{N}\frac{\left|1-e^{2\pi i\left(N\varphi-\left(b+d\right)\right)}\right|}{\left|1-e^{2\pi i\left(\varphi-\left(b+d\right)/N\right)}\right|}{% endequation %}

ההחלפה של {% equation %}j{% endequation %} ב-{% equation %}b+d{% endequation %} כאן בלי להכניס איזה {% equation %}\text{mod}N{% endequation %} היא לא טריוויאלית לגמרי; היא מוצדקת בכך שכפולה של {% equation %}N{% endequation %} במעריך של האקספוננט פשוט מובילה לתוספת כמות שלמה של {% equation %}2\pi i{% endequation %}, שמתורגם ל-1; בשלב הזה כבר השתמשנו בזה כמה פעמים ואני מקווה שזה ברור.

עכשיו, את המונה קל לחסום מלמעלה:

{% equation %}\left|1-e^{2\pi i\left(N\varphi-b+d\right)}\right|\le2{% endequation %}

למה? כי האקספוננט הזה, מפחיד ככל שיהיה, מתורגם בסו, למספר מרוכב מנורמה 1. אז אי שוויון המשולש נותן לנו {% equation %}\left|1-z\right|\le\left|1\right|+\left|z\right|=1+1=2{% endequation %}.

אז המונה קל, אבל את המכנה:

{% equation %}\left|1-e^{2\pi i\left(\varphi-\left(b+d\right)/N\right)}\right|{% endequation %}

צריך לחסום מלמטה. זה דורש קצת יותר. ראשית, בואו נחזיר לתמונה את

{% equation %}\delta=\varphi-\frac{b}{N}{% endequation %}

והביטוי שצריך לחסום יהפוך אל

{% equation %}\left|1-e^{2\pi i\left(\delta-d/N\right)}\right|{% endequation %}

עכשיו, {% equation %}\varphi-\frac{b+d}{N}=\delta-\frac{d}{N}{% endequation %}.

מכיוון ש-{% equation %}-\frac{N}{2}<d{% endequation %} אז {% equation %}-\frac{N}{2}+1\le d{% endequation %}, כלומר {% equation %}-\frac{1}{2}+\frac{1}{N}\le\frac{d}{N}{% endequation %}. בנוסף לכך {% equation %}\delta\le\frac{1}{N}{% endequation %} ולכן נקבל

{% equation %}\delta-\frac{d}{N}\le\frac{1}{N}+\frac{1}{2}-\frac{1}{N}=\frac{1}{2}{% endequation %}

ובאופן קצת יותר קל גם

{% equation %}\delta+\frac{d}{N}\ge0-\frac{1}{2}=-\frac{1}{2}{% endequation %}

מה שנותן לנו

{% equation %}-\pi\le2\pi\left(\delta-d/N\right)\le\pi{% endequation %}

בשביל מה זה טוב? כי בואו נסתכל שניה על הביטוי {% equation %}1-e^{i\theta}=1-\cos\theta-i\sin\theta{% endequation %} כאשר {% equation %}-\pi\le\theta\le\pi{% endequation %}. אני אצטרך קצת נוסחאות טריגונומטריות כדי לפשט אותו:

<ul> <li>{% equation %}1-\cos\theta=2\sin^{2}\frac{\theta}{2}{% endequation %}</li>


<li>{% equation %}\sin\theta=2\sin\frac{\theta}{2}\cos\frac{\theta}{2}{% endequation %}</li>

</ul>

לשמחתי אני סוף סוף יכול לומר <a href="https://gadial.net/2021/06/25/trigonometry_intro_3/">שיש לי פוסט</a> שמוכיח את הנוסחאות הללות ולכן לא אסביר אותן כאן שוב, אבל הן מפשטות יפה את הביטוי שלנו:

{% equation %}1-\cos\theta-i\sin\theta=2\sin^{2}\frac{\theta}{2}-2i\sin\frac{\theta}{2}\cos\frac{\theta}{2}=2\sin\frac{\theta}{2}\left(\sin\frac{\theta}{2}-i\cos\frac{\theta}{2}\right){% endequation %}

לכאורה זה יותר מסובך, אבל ערך מוחלט יפשט לנו את העניינים. בכללי, {% equation %}\left|a+bi\right|=\sqrt{a^{2}+b^{2}}{% endequation %}, ותוך ניצול העובדה ש-{% equation %}\sin^{2}\alpha+\cos^{2}\alpha=1{% endequation %}, נקבל

{% equation %}\left|2\sin\frac{\theta}{2}\left(\sin\frac{\theta}{2}-i\cos\frac{\theta}{2}\right)\right|=2\left|\sin\frac{\theta}{2}\right|\left|\sin\frac{\theta}{2}-i\cos\frac{\theta}{2}\right|=2\left|\sin\frac{\theta}{2}\right|{% endequation %}

עכשיו, בתחום {% equation %}0\le x\le\frac{\pi}{2}{% endequation %} סינוס מקיימת תכונה נחמדה מאוד: היא <strong>קעורה</strong>, כלומר הערכים שלה בין שתי נקודות גדולים יותר מהקו הישר שמחבר את שתי הנקודות הללו. נקודות הקצה של התחום הן {% equation %}\left(0,0\right){% endequation %} (ראשית הצירים) ו-{% equation %}\left(\frac{\pi}{2},1\right){% endequation %} (הקצה הימני של תחום העלייה של סינוס, כשהיא מגיעה ל-1 ומתחילה ליפול) ולכן הקו הישר המחבר את שתי הנקודות הללו הוא {% equation %}y=\frac{2}{\pi}x{% endequation %}, ואנו מקבלים ש-{% equation %}\sin x\ge\frac{2}{\pi}x{% endequation %}, כלומר בתחום הזה שבו הכל חיובי, {% equation %}\left|\sin x\right|\ge\frac{2}{\pi}\left|x\right|{% endequation %}.

עבור {% equation %}-\frac{\pi}{2}\le x\le0{% endequation %} זה טיפה יותר מסובך כי {% equation %}\left|x\right|=-x{% endequation %} במקרה הזה. עכשיו, {% equation %}\sin x{% endequation %} היא פונקציה אנטי-סימטרית, כלומר {% equation %}\sin\left(-x\right)=-\sin x{% endequation %}, ולכן עבור {% equation %}-\frac{\pi}{2}\le x\le0{% endequation %} נקבל

{% equation %}\left|\sin x\right|=-\sin x=\sin\left(-x\right)\ge\frac{2}{\pi}\left(-x\right)=\frac{2}{\pi}\left|x\right|{% endequation %}

ולכן קיבלנו את אי-השוויון {% equation %}\left|\sin x\right|\ge\frac{2}{\pi}\left|x\right|{% endequation %} עבור כל {% equation %}-\frac{\pi}{2}\le x\le0{% endequation %}.

עכשיו, אם {% equation %}-\pi\le\theta\le\pi{% endequation %} אז {% equation %}-\frac{\pi}{2}\le\frac{\theta}{2}\le\frac{\pi}{2}{% endequation %} ולכן אנו מקבלים

{% equation %}\left|1-e^{i\theta}\right|=2\left|\sin\frac{\theta}{2}\right|\ge2\cdot\frac{2}{\pi}\left|\frac{\theta}{2}\right|=\frac{2}{\pi}\left|\theta\right|{% endequation %}

ואפשר להתקדם הלאה. כזכור, אנחנו באמצע חסימה מלמטה של הביטוי

{% equation %}\left|1-e^{2\pi i\left(\delta-d/N\right)}\right|{% endequation %}

תוך שאנחנו יודעים ש-

{% equation %}-\pi\le2\pi\left(\delta-d/N\right)\le\pi{% endequation %}

כלומר, במקרה הזה {% equation %}\theta=2\pi\left(\delta-d/N\right){% endequation %}, ולכן נקבל

{% equation %}\left|1-e^{2\pi i\left(\delta-d/N\right)}\right|\ge4\left|\left(\delta-d/N\right)\right|{% endequation %}

עכשיו נחזור אל הדבר שממנו התחלנו - אנחנו מנסים לחסום מלמטה את הערך המוחלט של {% equation %}\beta_{d}{% endequation %}, שהיא האמפליטודה של תוצאה "לא טובה" בערכי ה-{% equation %}d{% endequation %} שאנו מסתכלים עליהם. תוך שימוש באי השוויון שהוכחנו זה עתה, נקבל

{% equation %}\left|\beta_{d}\right|\le\frac{1}{N}\frac{2}{\left|1-e^{2\pi i\left(\delta-d/N\right)}\right|}\le\frac{1}{N}\frac{2}{4\left|\left(\delta-d/N\right)\right|}=\frac{1}{4}\frac{1}{\left|\left(N\delta-d\right)\right|}{% endequation %}

וקיבלנו חסם על ההסתברות הכוללת לתוצאה "רעה":

{% equation %}p\left(\left|m-b\right|>e\right)\le\sum_{-N/2\le d<e}\left|\beta_{d}\right|^{2}+\sum_{e<d\le N/2}\left|\beta_{d}\right|^{2}{% endequation %}

{% equation %}\le\frac{1}{4}\left[\sum_{-N/2<d<-e}\frac{1}{\left(N\delta-d\right)^{2}}+\sum_{e<d\le N/2}\frac{1}{\left(N\delta-d\right)^{2}}\right]{% endequation %}

כן, כן, זה עדיין נראה מחריד ונצטרך לעבוד עוד כדי לפשט את זה. זו דרך החדו"א - כל הזמן מוצאים מה לפשט במחיר של {% equation %}\le{% endequation %} נוסף בדרך. עכשיו אפשר להתעסק עם ה-{% equation %}\delta{% endequation %} הזה שלמטה שהמהות שלו היא להיות קטן. כמה קטן? {% equation %}0\le\delta\le\frac{1}{N}{% endequation %}, כלומר {% equation %}0\le N\delta\le1{% endequation %}. זה אומר שאפשר להעלים את {% equation %}N\delta{% endequation %} מתוך {% equation %}\left(N\delta-d\right)^{2}{% endequation %} בצורה יחסית פשוטה - אבל כרגיל, נצטרך להיזהר. קודם כל נפתח סוגריים

{% equation %}\left(N\delta-d\right)^{2}=\left(N\delta\right)^{2}-2\left(N\delta\right)d+d^{2}=\left(N\delta\right)\left[N\delta-2d\right]+d^{2}{% endequation %}

אם {% equation %}d<0{% endequation %} אז גם {% equation %}N\delta+2d>0{% endequation %} ולכן {% equation %}\left(N\delta-d\right)^{2}>d^{2}{% endequation %}, כלומר {% equation %}\frac{1}{\left(N\delta-d\right)^{2}}<\frac{1}{d^{2}}{% endequation %}. זה מטפל באיברים של הסכום השמאלי.

אם {% equation %}d>0{% endequation %}, כלומר {% equation %}d\ge1{% endequation %} נעשה משהו אחר: נשתמש בכך ש-{% equation %}N\delta\le1{% endequation %} ולכן {% equation %}N\delta-d\le1-d{% endequation %}. עכשיו, שני האגפים בביטוי הזה הם שליליים (כי {% equation %}d\ge1{% endequation %}) ולכן כשנעלה אותם בריבוע כיוון האי שוויון יתהפך ונקבל {% equation %}\left(N\delta-d\right)^{2}\ge\left(1-d\right)^{2}{% endequation %}, ולכן {% equation %}\frac{1}{\left(N\delta-d\right)^{2}}\le\frac{1}{\left(1-d\right)^{2}}{% endequation %}.

לסיכום, קיבלנו את הצעד הבא בחסימה של הביטוי שלנו:

{% equation %}p\left(\left|m-b\right|>e\right)\le\frac{1}{4}\left[\sum_{-N/2<d<-e}\frac{1}{d^{2}}+\sum_{e<d\le N/2}\frac{1}{\left(d-1\right)^{2}}\right]{% endequation %}

אנחנו כבר לקראת הסוף! התעלול הבא הוא לאחד את שני הסכומים לסכום אחד כי בעצם מופיעים בהם כמעט אותם איברים בדיוק: בשמאלי מופיע {% equation %}\frac{1}{d^{2}}{% endequation %} לכל {% equation %}-\frac{N}{2}<d<-e{% endequation %} ובשני מופיע {% equation %}\frac{1}{\left(d-1\right)^{2}}{% endequation %} לכל {% equation %}e<d\le\frac{N}{2}{% endequation %}. כלומר, בשניהם מופיעים כל האיברים

{% equation %}\frac{1}{\left(e+1\right)^{2}},\frac{1}{\left(e+2\right)^{2}},\ldots,\frac{1}{\left(N/2-1\right)^{2}}{% endequation %}

ובנוסף בימני מופיע גם {% equation %}\frac{1}{e^{2}}{% endequation %}. אז בואו ניקח 2 כפול סכום כל האיברים הללו:

{% equation %}p\left(\left|m-b\right|>e\right)\le\frac{1}{2}\sum_{d=e}^{N/2-1}\frac{1}{d^{2}}{% endequation %}

זה כבר סכום ממש פשוט. טריק סטנדרטי כדי לחסום סכומים כאלו הוא לעבור מסכום לאינטגרל, ב"מחיר" של הגדלה קטנה של התחום התחתון:

{% equation %}\sum_{d=e}^{N/2-1}\frac{1}{d^{2}}\le\int_{e-1}^{N/2-1}\frac{1}{x^{2}}dx{% endequation %}

זה עובד כי מאחר ו-{% equation %}\frac{1}{x^{2}}{% endequation %} היא פונקציה יורדת, המינימום שלה מתקבל בסוף כל קטע, והאינטגרל של פונקציה על קטע כלשהו גדול או שווה למינימום שלה כפול אורך הקטע. במילים אחרות, {% equation %}\int_{d-1}^{d}\frac{1}{x^{2}}dx\ge\frac{1}{d^{2}}\cdot1{% endequation %}, ובצורה הזו אנחנו יכולים לחסום את כל אברי הסכום {% equation %}\sum_{d=e}^{N/2-1}\frac{1}{d^{2}}{% endequation %} על ידי חתיכות אינטגרלים מתאימות.

למה לעבור לאינטגרל עזר לנו? כי אינטגרלים יותר קל לנו לחשב במדויק:

{% equation %}\int_{e-1}^{N/2-1}\frac{1}{x^{2}}dx=\left[-\frac{1}{x}\right]_{e-1}^{N/2-1}=\frac{1}{e-1}-\frac{1}{N/2-1}\le\frac{1}{e-1}{% endequation %}

ולכן קיבלנו סוף כל סוף

{% equation %}p\left(\left|m-b\right|>e\right)\le\frac{1}{2\left(e-1\right)}{% endequation %}

וזה... ביטוי די פשוט!

<h2>סיכום רגוע יותר של כל העניין</h2>

עשיתי הרבה חישובים טכניים בחלק הקודם, אבל אפשר לסכם אותם בצורה די פשוטה: הראינו שההסתברות לקבל באלגוריתם הערכת הפאזה תוצאה לא טובה חסומה על ידי {% equation %}\frac{1}{2\left(e-1\right)}{% endequation %}, כש-{% equation %}e{% endequation %} הוא פרמטר שמשמש אותנו להערכת רמת הדיוק שלנו. רמת הדיוק תלויה לא רק בערך המספרי של {% equation %}e{% endequation %} אלא גם במספר הקיוביטים שאנחנו משתמשים בו ברגיסטר הראשון, {% equation %}n{% endequation %}. בואו ניכנס עכשיו להסבר יותר מפורט של מה שזה אומר.

המושג שאנחנו מדברים עליו הוא "רמת דיוק של {% equation %}k{% endequation %} ספרות אחרי הנקודה". בואו ניתן דוגמא פשוטה עם מספרים בייצוג עשרוני. אם {% equation %}a=0.2513{% endequation %} הוא מספר, ואנחנו מסתכלים על קירוב שלו ברמת דיוק של שתי ספרות אחרי הנקודה, הכוונה היא לכל מספר {% equation %}b{% endequation %} כך ש-{% equation %}\left|a-b\right|\le0.01{% endequation %}. אז למשל, {% equation %}a=0.25{% endequation %} הוא מספר כזה, אבל גם {% equation %}0.2433{% endequation %}, למרות שהוא לא מדויק בספרה השניה אחרי הנקודה, גם אם נעגל את המספר לשתי ספרות ונקבל {% equation %}0.24{% endequation %}. באופן כללי, דיוק ב-{% equation %}k{% endequation %} ספרות אחרי הנקודה פירושו {% equation %}\left|a-b\right|\le\frac{1}{10^{k}}{% endequation %}, אבל בהקשר שלנו, שבו המספרים מיוצגים בבסיס בינארי, הכוונה היא ל-{% equation %}\left|a-b\right|\le\frac{1}{2^{k}}{% endequation %}.

נניח שאנחנו רוצים לקבל רמת דיוק של {% equation %}k{% endequation %} ספרות אחרי הנקודה בהסתברות טובה יחסית. ברור שאנחנו חייבים להקצות לפחות {% equation %}n{% endequation %} קיוביטים לרגיסטר הראשון, אחרת אין לנו מספיק ספרות בשביל דיוק של {% equation %}k{% endequation %} ספרות. כל קיוביט נוסף מעבר לכך שנקצה לרגיסטר הראשון יעזור לנו לשפר את ההסתברות לקבלת תוצאה טובה, אז בואו נכתוב {% equation %}n=k+p{% endequation %}, כאשר {% equation %}p{% endequation %} הם "הקיוביטים הנוספים לצורך שיפור ההסתברות" ובסוף נראה מה יוצאת ההסתברות כתלות ב-{% equation %}p{% endequation %}.

מה שכבר ראינו הוא שיש מספר טבעי {% equation %}b{% endequation %} כלשהו כך ש-{% equation %}\frac{b}{2^{n}}{% endequation %} קירוב טוב של {% equation %}\varphi{% endequation %}, במובן זה ש-{% equation %}\left|\frac{b}{2^{n}}-\varphi\right|\le\frac{1}{2^{n}}{% endequation %}, והיתרון של ה-{% equation %}b{% endequation %} הזה היה שיכלנו לחסום את המרחק של תוצת אלגוריתם הערכת הפאזה ממנו: האלגוריתם מחזיר מספר טבעי {% equation %}m{% endequation %} (שאנחנו חושבים עליו בתור דרך אחרת לכתוב את המספר {% equation %}\frac{m}{2^{n}}{% endequation %} שהוא הקירוב של {% equation %}\varphi{% endequation %} שאנו מחפשים) שההסתברות שיקיים {% equation %}\left|m-b\right|>e{% endequation %} קטנה או שווה ל-{% equation %}\frac{1}{2\left(e-1\right)}{% endequation %} שהזכרתי קודם. היופי הוא שה-{% equation %}e{% endequation %} נתון לבחירתנו בהתאם למה שנוח לנו.

אם אנחנו רוצים דיוק של {% equation %}k{% endequation %} ספרות, מה שנעשה הוא להגדיר {% equation %}e=2^{n-k}-1{% endequation %}. אם {% equation %}\left|m-b\right|\le e{% endequation %} אז

{% equation %}\left|\frac{m}{2^{n}}-\varphi\right|\le\left|\frac{m}{2^{n}}-\frac{b}{2^{n}}\right|+\left|\frac{b}{2^{n}}-\varphi\right|=\frac{1}{2^{n}}\left|m-b\right|+\left|\frac{b}{2^{n}}-\varphi\right|\le{% endequation %}

{% equation %}\le\frac{1}{2^{n}}\left(2^{n-k}-1\right)+\frac{1}{2^{n}}=\frac{2^{n-k}}{2^{n}}=\frac{1}{2^{k}}{% endequation %}

וזה בדיוק מה שרצינו. כעת, מה הסתברות <strong>הכישלון</strong>, כלומר ההסתברות שלא ניפול על {% equation %}m{% endequation %} טוב שכזה, בהינתן ה-{% equation %}e{% endequation %} שבחרנו? ראשית, ההסתברות היא לכל היותר {% equation %}\frac{1}{2\left(e-1\right)}{% endequation %}. כעת, נציב {% equation %}e=2^{n-k}-1{% endequation %} ונקבל את הסתברות הכישלון

{% equation %}\frac{1}{2\left(2^{n-k}-2\right)}=\frac{1}{2\left(2^{p}-2\right)}{% endequation %}

עבור {% equation %}p=0,1{% endequation %} מקבלים תוצאה שהיא שלילית או אינסוף - זה מפני שהחישוב עבור {% equation %}e{% endequation %} הניח במובלע שהוא לא מספר 0 או 1 בעצמו. אבל עבור {% equation %}p=2{% endequation %} מקבלים כבר תוצאה הגיונית - {% equation %}\frac{1}{4}{% endequation %}. עבור {% equation %}p=3{% endequation %} מקבלים {% equation %}\frac{1}{12}{% endequation %}, עבור {% equation %}p=4{% endequation %} מקבלים {% equation %}\frac{1}{28}{% endequation %} וכן הלאה - ככל שמוסיפים יותר קיוביטים, ההסתברות לקבל הערכה לא טובה שואפת אקספוננציאלית לאפס. אנחנו כמובן רוצים לדעת <strong>עד כמה</strong> זה שואף לאפס - מה צריך להיות {% equation %}p{% endequation %} אם אנחנו רוצים להקטין את הסתברות הכשלון כרצוננו? אז יהא {% equation %}\varepsilon>0{% endequation %} מספר כלשהו. כדי שהסתברות הכישלון תהיה קטנה מ-{% equation %}\varepsilon{% endequation %} צריך להתקיים

{% equation %}\frac{1}{2\left(2^{p}-2\right)}\le\varepsilon{% endequation %}

נכפול את שני האגפים ב-{% equation %}2^{p}-2{% endequation %} ונחלק ב-{% equation %}\varepsilon{% endequation %} ונקבל

{% equation %}2^{p}-2\ge\frac{1}{2\varepsilon}{% endequation %}

נעביר את {% equation %}2{% endequation %} אגף:

{% equation %}2^{p}\ge2+\frac{1}{2\varepsilon}{% endequation %}

ניקח {% equation %}\lg{% endequation %} (לוגריתם על בסיס 2) לשני האגפים ונקבל

{% equation %}p\ge\lg\left(2+\frac{1}{2\varepsilon}\right){% endequation %}

וזו הנוסחה שרצינו: אם אנחנו רוצים להבטיח הסתברות כישלון קטנה מ-{% equation %}\varepsilon{% endequation %}, נזדקק ל-{% equation %}\left\lceil \lg\left(2+\frac{1}{2\varepsilon}\right)\right\rceil {% endequation %} קיוביטים (זה הסימן לערך מוחלט <strong>עליון</strong>, לעגל כלפי מעלה) וזאת בנוסף ל-{% equation %}k{% endequation %} הקיוביטים שאמרנו ש"חייבים". 

אז לסיכום הכולל: כדי לקבל באלגוריתם הערכת הפאזה קירוב עם דיוק של {% equation %}k{% endequation %} ספרות בינאריות אחרי הנקודה בהסתברות של לפחות {% equation %}1-\varepsilon{% endequation %} צריך להשתמש ב-

{% equation %}n=k+\left\lceil \lg\left(2+\frac{1}{2\varepsilon}\right)\right\rceil {% endequation %} קיוביטים.

זה סוגר את האלגוריתם, אבל עדיין נותרה השאלה הפתוחה - בשביל מה זה טוב? והאלגוריתם של שור נותן לזה תשובה מוחצת וחד משמעית, ועוד מעז לעשות את זה עם שימוש יפהפה ולא טריוויאלי בכלל בהערכת פאזה, כך שנחכה עם זה לפוסט הבא. 
