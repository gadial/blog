---
title: "עוגה עוגה עוגה (נתהפכה כל היום עד אשר נמצא מקום)"
layout: post
categories:
  - משחקים וחידות מתמטיות
tags:
  - חידה מתמטית
---

בפוסט הזה אני רוצה לדבר על חידה שנראית תמימה למדי ממבט ראשון, אבל למעשה היא ערמומית מאוד ובצורה הטובה ביותר - כנראה יש לה יותר סיכוי להפיל בפח דווקא את פותרי החידות המשופשפים יותר, שכבר פיתחו אינטואיציה לא רעה שיש סיכוי טוב שתבגוד בהם בצורה אכזרית עם החידה הזו (או לפחות, זה מה שקרה <strong>לי</strong>).

החידה הולכת ככה: יש לנו עוגה, כלומר מעגל מושלם, ואנחנו חותכים ממנה פלחים <strong>והופכים</strong> כל פלח שחתכנו. זו עוגה עם ציפוי שוקולד למעלה, אבל למטה אין לה כלום. והשאלות שנשאלות הן:

<ol> <li>אחרי כמה זמן כל הציפוי יהיה שוב למעלה כמו שהיה בהתחלה?</li>


<li>אחרי כמה זמן כל הציפוי יהיה למטה, כלומר הכל התהפך?</li>

</ol>

בואו נסביר את הפרטים המדויקים. מה שאנחנו עושים הוא זה: קודם כל אנחנו חותכים את העוגה בחתך שמגיע מהשפה שלה עד למרכז ("רדיוס"). אחר כך אנחנו יוצרים חתך נוסף, שיוצר זווית {% equation %}\theta{% endequation %} עם החתך הקודם. עכשיו יש לנו פלח עוגה - כל מה שנמצא בין שני החתכים שחתכנו. אנחנו מוציאים את הפלח הזה בזהירות מהעוגה, הופכים אותו, ואז מכניסים אותו שוב בזהירות לתוך העוגה. ואז אנחנו זזים בזווית {% equation %}\theta{% endequation %} שוב, חותכים שוב, והופכים את הפלח החדש שקיבלנו (שאחד הגבולות שלו הוא גבול של הפלח הקודם) וכן הלאה וכן הלאה.

הנה איור שמתאר את המהומה הזו עבור {% equation %}\theta=\frac{\pi}{2}{% endequation %} ("90 מעלות"):

<img src="{{site.baseurl}}{{site.post_images}}/2025/cake_cutting_1.png" alt=""/>

בכל פעם שאני הופך פלח עוגה, אני קורא לזה "צעד". אז אנחנו רואים שבמקרה הזה, אחרי ארבעה צעדים כל הציפוי יהיה למטה, ואחרי שמונה צעדים כל הציפוי יהיה למעלה. זו התשובה לחידה במקרה הזה. אבל המקרה הזה בבירור פשוט למדי - עבור זוויות אחרות די ברור שיהיו סיטואציות מסובכות יותר כמו זו שבה הפלח שחתכנו כרגע הוא חתיכה שכבר חתכנו בעבר , אז לכאורה כשננסה להפוך אותו הוא יתפרק לשניים והכל יימרח בכל מקום... אז בואו נניח שאנחנו יודעים להפוך פלחים-עם-חתכים בצורה מושלמת, כאילו הם הצליחו להידבק אחד לשני מחדש. עכשיו אפשר לשאול את השאלה עבור זווית קונקרטית לגמרי, למשל {% equation %}\theta=e^{-10}{% endequation %} כאשר {% equation %}e=2.718\ldots{% endequation %} הוא בסיס הלוגריתם הטבעי המוכר. כאן אני מודד זוויות עם <a href="https://gadial.net/2021/08/18/trigonometry_intro_6/">רדיאנים</a>, כלומר בכל צעד אני עובר {% equation %}\frac{\theta}{2\pi}=\frac{1}{2\pi e^{10}}{% endequation %} מעגל.

אוקיי, אז מה התשובה? בואו נצא להפסקה. אני <strong>ממליץ מאוד בחום</strong> לא לקרוא את ההמשך לפני שניסיתם לפתור את החידה בעצמכם. בלי זה, זה פשוט לא יהיה כיף. אני לא אומר שהחידה בהכרח תצליח לעבוד עליכם; בהחלט ייתכן שתצליחו להגיע לפתרון עצמאית, אבל אז זה רק עוד יותר כיף, לא? בינתיים הנה צילום מסך ממשחק הניינטיז שבו נתקלתי בחידה הזו לראשונה:

<img src="{{site.baseurl}}{{site.post_images}}/2025/cake_cutting_2.png" alt=""/>

אוקיי, כולנו חשבנו על החידה? אפשר להמשיך ולהתחיל לספיילר חופשי? יופי. ראשית - לא, אין שום משחק ניינטיז (ועכשיו קצת עצוב לי שאין), זו תמונה מג'ונרטת מן הסתם. שנית, מה שהאינטואיציה שלי הולכת אליו מייד בהקשר של החידה הזו הוא טיעון שמבוסס על <strong>אי רציונליות</strong> שבא להוכיח שהציפוי אף פעם לא יחזור כולו למעלה או יגיע כולו למטה. העניין הוא כזה - אם אני מטייל לי מסביב לעוגה בצעדים שכל אחד מהם עובר בדיוק {% equation %}\omega{% endequation %}-מעגל כש-{% equation %}\omega{% endequation %} הוא מספר אי רציונלי אז כשאני מסיים סיבוב סביב העוגה אני לא אחזור בדיוק למקום שממנו התחלתי. גם לא בפעם השניה. או השלישית. או כל פעם אפשרית. כי אם <strong>מתישהו</strong> חזרתי לנקודת ההתחלה, נאמר אחרי {% equation %}k{% endequation %} צעדים ו-{% equation %}t{% endequation %} הקפות של המעגל, אז צריך להתקיים {% equation %}k\omega=t{% endequation %} כלומר {% equation %}\omega=\frac{t}{k}{% endequation %} מה שמראה שהוא רציונלי. זה מה שיקרה, למשל, אם {% equation %}\theta=\frac{4\pi}{3}{% endequation %}, כלומר אם בכל פעם אנחנו עוברים 240 מעלות מהמעגל, שזה {% equation %}\frac{2}{3}{% endequation %} ממנו: נצטרך {% equation %}k=3{% endequation %} צעדים כדי להגיע לנקודת ההתחלה בסיום הקפה מספר {% equation %}t=2{% endequation %} של המעגל.

האם במקרה שלנו {% equation %}\omega{% endequation %} הוא אי רציונלי? לכאורה כן, הרי השתמשנו ב-{% equation %}e^{-10}{% endequation %} המאוד לא רציונלי בהגדרה שלו. אבל {% equation %}\omega{% endequation %} (החלק היחסי של המעגל שאנחנו עוברים בכל פעם) הוא {% equation %}\omega=\frac{\theta}{2\pi}=\frac{1}{2\pi e^{10}}{% endequation %} ולכן מעורבת כאן השאלה האם {% equation %}\pi e^{10}{% endequation %} זה גם כן מספר אי רציונלי וזו... שאלה פתוחה, ככל שידוע לי.

העניין הוא שכל זה לא חשוב. כל מערך השיקולים הזה בכלל לא רלוונטי. החידה הרבה יותר פשוטה מזה ולא מצריכה שום מתמטיקה מתוחכמת. סתם סיבכתי את עצמי עם שיקולים לא רלוונטים כי אלוהים אדירים כמה שהתרגלתי כבר לשלוף את טיעון האי רציונליות הזה מהשרוול בכל פעם מחדש.

אז מה העניין? העניין הוא שלא חשוב בכלל אם אנחנו חוזרים לנקודת ההתחלה או לא, הדבר היחיד שחשוב הוא האם אנחנו חותכים את העוגה כל פעם במקום שטרם נחתך, או שיש רק מספר <strong>סופי</strong> של חתכים שהולכים להיות בעוגה ולא משנה כמה פעמים נחזור על התהליך? התשובה היא שיהיה מספר סופי של חתכים, ואפילו די קטן. ואיך זה ייתכן, אם אנחנו עושים סיבובים מסביב לעוגה ולא חוזרים אף פעם לנקודה שממנו התחלנו? אה, פשוט מאוד: כי <strong>החתכים זזים</strong> כשאנחנו הופכים את העוגה. זה לב העניין פה, ומה שקל לפספס כשמנסים לפתור את החידה בצורה נאיבית.

אם יש לנו פלח עוגה שכבר יש בו חתך, ואנחנו מרימים את כולו והופכים אותו, החתך לא יישאר במקום שבו הוא היה קודם - הוא יעבור לצד השני, כאילו הפעלנו עליו שיקוף במראה שנמצאת בדיוק באמצע הפלח. הנה הדגמה של איך זה נראה, כשהזווית שבה אנו זזים בכל פעם היא 270 מעלות:

<img src="{{site.baseurl}}{{site.post_images}}/2025/cake_cutting_3.png" alt=""/>

הפלח הראשון שנוצר הוא של שלושת-רבעי עוגה, והחתכים שהם הגבולות שלו הם הרדיוס האופקי שמגיע מימין (זה החיתוך הראשון) והרדיוס האנכי שעולה למעלה. הפלח השני עדיין משתמש ברדיוס האנכי שעולה למעלה, אבל החתך הנוסף שלו הוא הרדיוס האופקי שמגיע משמאל (ומצוייר בקו מקווקוו באיור). אני מסמן בירוק את החתך שהוא הרדיוס האופקי שמגיע מימין. הוא נמצא <strong>בתוך</strong> פלח העוגה השני שאנחנו הופכים, ואחרי ההיפוך הוא ישנה מקום ויהפוך להיות רדיוס אנכי שיורד למטה. התזוזה הזו של החתכים היא תשבטיח שמהר מאוד נחתוך רק בתוך חתכים שכבר חתכנו קודם.

עכשיו בואו נדבר פחות באוויר ונראה את המתמטיקה הקונקרטית שמעורבת, ואיך אפשר למצוא אחרי כמה זמן הכל יחזור למעלה. בואו נתחזק קבוצה {% equation %}A{% endequation %} שכוללת את כל הזוויות שבהם יש חתכים בעוגה. בהתחלה הקבוצה הזו ריקה, {% equation %}A=\emptyset{% endequation %}. החתך הראשון קובע את נקודת הייחוס שעל פיה אנחנו מודדים את הזווית של שאר החתכים, אז אחריו {% equation %}A=\left\{ 0\right\} {% endequation %}. החתך הבא יהיה בזווית של {% equation %}\theta{% endequation %} ביחס אליו, אז {% equation %}A=\left\{ 0,\theta\right\} {% endequation %}, ועכשיו אנחנו מתקדמים כל פעם ב-{% equation %}\theta{% endequation %}, כך שהקבוצה שלנו היא לכאורה {% equation %}A=\left\{ 0,\theta,2\theta,3\theta,\ldots\right\} {% endequation %}. אבל <strong>זה לא נמשך עד אינסוף ככה</strong>. מרגע שבו נשלים את הסיבוב הראשון סביב העוגה הסיפור יתחיל להסתבך, אז אנחנו צריכים להבין מתי בדיוק זה קורה.

בואו נסמן ב-{% equation %}k{% endequation %} את מספר החתך הראשון שבו אנחנו אחרי סיבוב שלם סביב העוגה. כלומר, {% equation %}k\theta\ge2\pi{% endequation %} אבל {% equation %}\left(k-1\right)\theta<2\pi{% endequation %}. יש במתמטית דרך פשוטה להגדיר את {% equation %}k{% endequation %}: {% equation %}k=\left\lceil \frac{2\pi}{\theta}\right\rceil {% endequation %} (הסוגריים הללו מציינים <strong>ערך שלם עליון</strong>: אנחנו מעגלים למספר השלם הקרוב ביותר שגדול מ-{% equation %}\frac{2\pi}{\theta}{% endequation %}). עכשיו, תהיה חשיבות גדולה לשאלה כמה החתך ה-{% equation %}k{% endequation %} חורג "מעבר" לסיבוב שלם - מה ההפרש בין נקודת החיתוך הזו ונקודת הייחוס שלנו שסימנתי ב-{% equation %}0{% endequation %}. אז אני אסמן את ההפרש הזה ב-{% equation %}\delta{% endequation %}: {% equation %}\delta=k\theta-2\pi{% endequation %}. זהו, אלו כל הסימונים שנזדקק להם. כל הפתרון עכשיו יהיה במונחים של {% equation %}k,\delta{% endequation %}. עכשיו, המקרה שבו {% equation %}\delta=0{% endequation %} הוא פשוט <strong>מדי</strong> - כבר ראינו אותו למעלה. תוך סיבוב אחד כל העוגה הפוכה ותוך סיבוב אחד נוסף היא חוזרת לעצמה. אז נעזוב את המקרה הזה ונניח ש-{% equation %}\delta>0{% endequation %}.

רגע <strong>לפני</strong> החיתוך הגורלי הזה, קבוצת החיתוכים שלנו היא

{% equation %}A=\left\{ 0,\theta,2\theta,\ldots,\left(k-1\right)\theta\right\} {% endequation %}

רגע אחריו קורים שני דברים. ראשית, אני מוסיף חיתוך ב-{% equation %}\delta{% endequation %} (כלומר, החיתוך הוא ב-{% equation %}\theta k{% endequation %} אבל מכיוון שעברנו את קו הגבול של {% equation %}2\pi{% endequation %} אנחנו עושים את כל החשבון מודולו {% equation %}2\pi{% endequation %}). שנית, עכשיו החתך 0 "כלוא" בין החתך ב-{% equation %}\left(k-1\right)\theta{% endequation %} ו-{% equation %}\delta{% endequation %} ולכן כשהופכים את הפלח שבו הוא נמצא, הוא הולך <strong>להשתנות</strong>. הוא כבר לא יהיה 0. הוא יהיה... אה... אוקיי, זה חישוב מעצבן, מה? יודעים מה, בואו נשנה טיפה את דרך ההצגה של הסיפור כדי שיהיה לי קל יותר לבצע את החישוב הזה.

בואו נדמיין לרגע סיטואציה פשוטה יותר: יש לי פלח ששתי נקודות הקצה שלו הן 0 ו-{% equation %}\theta{% endequation %} ובתוכו כלוא חתך אחר שנמצא ב-{% equation %}x{% endequation %}. לאן הוא עובר כשהופכים את הפלח? קודם המרחק שלו מהחתך 0 היה {% equation %}x{% endequation %}; אחרי ההיפוך, החתך 0 נמצא במקום {% equation %}\theta{% endequation %}; היפוך שומר על מרחקים, אז החתך הכלוא עדיין במרחק {% equation %}x{% endequation %} מהחתך 0-לשעבר, כלומר הוא חייב להיות ב-{% equation %}\theta-x{% endequation %} (כי {% equation %}\theta+x{% endequation %} בכלל לא במסגרת הפלח הזה). זה היה חישוב פשוט! אבל לחשב לאן עובר מי שכלוא בין {% equation %}\left(k-1\right)\theta{% endequation %} ו-{% equation %}\delta{% endequation %} זה כאב ראש כשזוכרים שצריך לעבוד מודולו, ושכל הזמן הקואורדינטות של הפלח הנוכחי ישתנו. אז במקום זה בואו נחשוב על הסיטואציה ככה: אני תמיד חותך את החתך הנוכחי שלי ב-0; ואחרי כל חתך והיפוך פלח אני <strong>מסובב את העוגה</strong> ב-{% equation %}\theta{% endequation %}, בצורה כזו שמוסיפה {% equation %}\theta{% endequation %} לכל זווית.

בגישה הזו, האלגוריתם שלוקח את {% equation %}A{% endequation %} ומרחיב אותה על ידי הוספת החתך החדש, תוך תיקון חתכים ש"מתהפכים" עובד כך:

<ol> <li>נאתחל {% equation %}A=\emptyset{% endequation %}</li>


<li>נחזור שוב ושוב על הפעולה הבאה:</li>
<ol>


<li>נאתחל {% equation %}A^{\prime}=\left\{ 0\right\} {% endequation %} (אלו יהיו החתכים החדשים, אחרי הצעד שאנחנו עושים, ובפרט יהיה ב-{% equation %}A^{\prime}{% endequation %} את החתך שעשינו ב-0)</li>


<li>לכל {% equation %}x\in A{% endequation %} נעשה:</li>
<ol>


<li>אם {% equation %}0<x<\theta{% endequation %} אז {% equation %}x\leftarrow\theta-x{% endequation %} (כלומר, אני מציב את הערך החדש בתוך {% equation %}x{% endequation %}; זה ההיפוך של חתך "כלוא").</li>


<li>נוסיף את {% equation %}\left(x+\theta\right)\text{ mod }2\pi{% endequation %} אל {% equation %}A^{\prime}{% endequation %} (זה הסיבוב שמבצעים אחרי החיתוך וההיפוך).</li>
</ol>

<li>אם {% equation %}A^{\prime}=A{% endequation %}, נעצור. אחרת {% equation %}A\leftarrow A^{\prime}{% endequation %}.</li>
</ol>
</ol>

עם איזה {% equation %}A{% endequation %} נסיים בסופו של דבר? מכיוון שכל הזמן אנחנו מוסיפים את 0, יהיה ב-{% equation %}A{% endequation %} כל הזמן את 0, ואת כל ההזזות של {% equation %}0{% endequation %} עד שעוברים את {% equation %}2\pi{% endequation %}, כלומר {% equation %}\left\{ 0,\theta,2\theta,\ldots,\left(k-1\right)\theta\right\} {% endequation %} שראינו קודם. בנוסף לכך, כשניקח את {% equation %}\left(k-1\right)\theta{% endequation %} ונוסיף לו {% equation %}\theta{% endequation %} נקבל {% equation %}\delta{% endequation %}. עכשיו, שימו לב! ה-{% equation %}\delta{% endequation %} הזה כלוא בדיוק בפלח שהולכים להפוך כי {% equation %}0<\delta<\theta{% endequation %}. לכן ההיפוך הולך להפוך אותו ל-{% equation %}\theta-\delta{% endequation %} ומייד אחר כך הסיבוב יביא אותו אל {% equation %}2\theta-\delta{% endequation %}. עכשיו הוא כבר חמק מהפלח שהופכים, ולכן לא יתהפך שוב אלא ימשיך להסתובב עוד ועוד. נקבל את {% equation %}3\theta-\delta{% endequation %} ואת {% equation %}4\theta-\delta{% endequation %} וכן הלאה וכן הלאה עד שנגיע שוב להשלמה של סיבוב, וזה יהיה ב-{% equation %}\left(k-1\right)\theta-\delta{% endequation %}. מייד אחר כך נגיע אל {% equation %}k\theta-\delta=2\pi{% endequation %}, כלומר חזרה אל 0. בינגו! איכשהו <strong>כן</strong> חזרנו אל נקודת המוצא שלנו, אפילו אם {% equation %}\theta{% endequation %} הוא אי רציונלי, אחרי בדיוק שתי הקפות סביב המעגל. איך זה קרה? אז כאמור, זה לא באמת קרה כי שיניתי את נקודת המבט שלי - עכשיו אני בכל פעם מסובב את העוגה כך שהחתך שאני עושה הוא ב-0. זה אומר שאולי אני חותך כל פעם בזווית שונה, אבל בגלל האופן שבו החתכים זזים החיתוכים שלי הם רק בתוך חתכים קיימים.

אז בגישה הנוכחית שלנו לזוויות, קבוצת כל החתכים הולכת להיות

{% equation %}A=\left\{ 0,\theta,2\theta,\ldots,\left(k-1\right)\theta,\delta,2\theta-\delta,\ldots,\left(k-1\right)\theta-\delta\right\} {% endequation %}

בקבוצה הזו יש בסך הכל {% equation %}2k-1{% endequation %} חתכים, והם מגדירים {% equation %}2k-1{% endequation %} פלחים שאפשר לכתוב במפורש:

{% equation %}\left[0,\delta\right],\left[\delta,\theta\right],\left[\theta,2\theta-\delta\right],\left[2\theta-\delta,2\theta\right],\ldots,\left[\left(k-2\right)\theta,\left(k-1\right)\theta-\delta\right],\left[\left(k-1\right)\theta-\delta,\left(k-1\right)\theta\right],\left[\left(k-1\right)\theta,0\right]{% endequation %}

יש כאן שני סוגים של פלחים: כאלו שהאורך שלהם הוא {% equation %}\delta{% endequation %}, וכאלו שהאורך שלהם הוא {% equation %}\theta-\delta{% endequation %}. הפלחים מהסוג הראשון הם

{% equation %}\left[0,\delta\right],\left[\theta,2\theta-\delta\right],\left[2\theta,3\theta-\delta\right],\ldots,\left[\left(k-1\right)\theta,0\right]{% endequation %}

וכאן יש {% equation %}k{% endequation %} פלחים סך הכל, והפלחים מהסוג השני הם

{% equation %}\left[\delta,\theta\right],\left[2\theta-\delta,2\theta\right],\ldots,\left[\left(k-1\right)\theta-\delta,\left(k-1\right)\theta\right]{% endequation %}

וכאן יש {% equation %}k-1{% endequation %} פלחים.

על מצב העוגה בכל רגע נתון אפשר לחשוב בתור סימון, לכל פלח, האם הוא הפוך באותו רגע או לא ("וקטור בינארי מאורך {% equation %}2k-1{% endequation %}). עכשיו מגיע הפאנץ': בכל פעם שבה אנחנו מבצעים חתך והופכים את העוגה, אנחנו הופכים פלח בגודל {% equation %}\theta{% endequation %} שמורכב משני תת-פלחים, אחד מגודל {% equation %}\delta{% endequation %} והשני מגודל {% equation %}\theta-\delta{% endequation %}. אחרי שביצענו {% equation %}k{% endequation %} צעדים הפכנו את כל ה-{% equation %}\delta{% endequation %}-פלחים, ואחרי שנבצע עוד {% equation %}k{% endequation %} צעדים נהפוך את כולם בחזרה וכן הלאה; אבל עבור ה-{% equation %}\theta-\delta{% endequation %}-פלחים, זה יקרה כל {% equation %}k-1{% endequation %} צעדים, לא כל {% equation %}k{% endequation %} צעדים. כלומר, כדי שכל הפלחים בעוגה יתהפכו בחזרה, אנחנו צריכים שמספר הצעדים הכולל שלנו {% equation %}T{% endequation %} יהיה <strong>כפולה זוגית</strong> גם של {% equation %}k{% endequation %} וגם של {% equation %}k-1{% endequation %}. כפולה, כדי שהוא יעבור על כל הפלחים מאותו סוג אותו מספר פעמים; זוגית כי אחרי שעוברים מספר זוגי של פעמים על פלח מחזירים אותו למצב המקורי שלו.

עכשיו, {% equation %}k,k-1{% endequation %} הם מספרים <strong>זרים</strong> - אין להם מחלק משותף גדול מ-1. זה אומר שהמספר הקטן ביותר שמתחלק על ידי שניהם (מה שנקרא ה-lcm שלהם) הוא המכפלה שלהם, {% equation %}k\left(k-1\right){% endequation %}. המכפלה הזו היא מספר זוגי, אבל היא לא <strong>כפולה זוגית</strong> שלהם, כלומר זה לא מספר שמתקבל על ידי כך שמכפילים אותם במספר <strong>זוגי</strong>. למשל, אם {% equation %}k{% endequation %} אי זוגי אז {% equation %}k\left(k-1\right){% endequation %} מתקבל מ-{% equation %}k-1{% endequation %} על ידי כפל שלו ב-{% equation %}k{% endequation %} שאיננו מספר זוגי. אז אם נבצע {% equation %}k\left(k-1\right){% endequation %} צעדים, נראה שכל הפלחים בעוגה מסוג אחד הם למעלה, וכל הפלחים מהסוג השני הם למטה. הכפולה <strong>הזוגית</strong> הקטנה ביותר היא {% equation %}2k\left(k-1\right){% endequation %}.

אם נחזור למספר הקונקרטי שהתחלתי איתו, {% equation %}\theta=e^{-10}{% endequation %}, החישוב עכשיו הוא מאוד פשוט: מחשבים את {% equation %}k=\left\lceil \frac{2\pi}{\theta}\right\rceil {% endequation %} ואז את {% equation %}2k\left(k-1\right){% endequation %}. מקבלים {% equation %}k=138397{% endequation %} ו-{% equation %}2k\left(k-1\right)=38307182424{% endequation %}. אלו לא מספרים שיש להם משמעות מעניינת, אבל אם פתרתן את החידה קודם וקיבלתן תוצאה מספרית, אפשר להשוות אותה למה שאני קיבלתי.

אוקיי, זה טיפל בשאלה מתי כל הציפוי חוזר <strong>למעלה</strong>. מה עם הגעה של כל הציפוי <strong>למטה</strong>? גם פה האינטואיציה הולמת בי - האינטואיציה הראשונית היא שזה צריך להיות בדיוק באמצע הדרך, כלומר לקחת את התוצאה שקיבלתי ולחלק ב-2. האינטואיציה הזו <strong>נכונה</strong> בדוגמא שראינו למעלה עם {% equation %}\theta=\frac{\pi}{2}{% endequation %}, אבל כמו שאמרתי, הדוגמא הזו הייתה פשוטה <strong>מדי</strong>; בחרתי בכוונה מקרה שבו {% equation %}\delta=0{% endequation %}. כאשר {% equation %}\delta>0{% endequation %} כבר ראינו שאמצע הדרך, {% equation %}k\left(k-1\right){% endequation %}, לא הולך לעבוד כי חצי מהעוגה יהיה הפוך וחצי לא. אז מה כן יעבוד? אנחנו צריכים מספר שהוא כפולה <strong>אי זוגית</strong> של {% equation %}k,\left(k-1\right){% endequation %}, אבל זה פשוט <strong>בלתי אפשרי</strong>. כל כפולה של {% equation %}k,\left(k-1\right){% endequation %} תתחלק על ידי הכפולה המשותפת הקטנה ביותר {% equation %}k\left(k-1\right){% endequation %} והיא תמיד מספר זוגי; מצד שני, אחד מבין {% equation %}k,\left(k-1\right){% endequation %} הוא אי זוגי ולכן כשנכפול אותו במספר אי זוגי נקבל מספר אי זוגי. אז פשוט <strong>לא קיימת</strong> כפולה אי זוגית משותפת של {% equation %}k,\left(k-1\right){% endequation %} והציפוי אף פעם לא יהיה כולו למטה.

מרהיב בעיני איך התחלתי עם מחשבה על שיקולי אי רציונליות וסיימתי עם שיקולי זוגיות מהסוג הפשוט ביותר. ככה חידות מתמטיות מוצלחות עובדות. 