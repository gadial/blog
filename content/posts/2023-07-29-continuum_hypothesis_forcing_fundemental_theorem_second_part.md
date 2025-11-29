---
title: "בעקבות השערת הרצף, חלק ח': המשפט היסודי של תורת הכפיה (המקרה הכללי)"
layout: post
categories:
  - תורת הקבוצות
tags:
  - השערת הרצף
image: "/assets/img/main/forcing.png"

---


<h2>מבוא</h2>

בפוסט הקודם הצגתי את המשפט היסודי של תורת הכפיה והוכחתי מקרה פרטי אחד שלו, המסובך ביותר, שיהווה בסיס ליתר ההוכחה. הפעם נתחיל מלסיים את כל ההוכחה, אבל כמובן שכדאי להיזכר על מה בעצם אנחנו מדברים.

כזכור, יש לנו "יקום מתמטי זעיר" {% equation %}\mathcal{M}{% endequation %} שהוא קבוצה בת מניה וטרנזיטיבית שאפשר להניח עליה (במובן ניואנסי מסוים שכבר חפרתי עליו בעבר) שמקיימת את אקסיומות ZFC. על היקום הזה אנחנו מלבישים קבוצה של "תנאי כפייה" {% equation %}P\in\mathcal{M}{% endequation %} שנבחרים בהתאם למטרה הספציפית שאנחנו רוצים להשיג, אבל בינתיים אנחנו מתייחסים אליהם באופן כללי. עכשיו, בהינתן {% equation %}P{% endequation %} אפשר לבנות קבוצה כלשהי {% equation %}G\subseteq P{% endequation %} שנקראת <strong>אידאל גנרי</strong> שיש לה מבנה עשיר מסוים שאנחנו רוצים להוסיף אל {% equation %}\mathcal{M}{% endequation %}. הראינו איך לעשות את זה - לבנות קבוצה חדשה {% equation %}\mathcal{M}\left[G\right]{% endequation %} בתהליך דו-שלבי שבו ראשית בנינו באופן בלתי תלוי ב-{% equation %}G{% endequation %} קבוצה של איברים של {% equation %}\mathcal{M}{% endequation %} שנקראו "שמות-{% equation %}P{% endequation %}"; ושנית, הראינו דרך בהינתן שם-{% equation %}P{% endequation %} {% equation %}\sigma{% endequation %} לקבל ממנו קבוצה {% equation %}\sigma^{G}{% endequation %} באופן שבו {% equation %}G{% endequation %} "מסננת" איברים מיותרים מתוך {% equation %}\sigma{% endequation %}. כל זה התרחש עוד לפני הפוסט האחרון.

בפוסט האחרון התחלנו להתעסק בשאלה "איזה תכונות היקום {% equation %}\mathcal{M}\left[G\right]{% endequation %} מקיים, וחשוב מכך - <strong>למה</strong> הוא מקיים אותן?" וטענו טענה שהיא די מרחיקת לכת, אפילו אם לא לגמרי ברור עד כמה - שאם נוסחה {% equation %}\phi\left(\tau_{1},\ldots,\tau_{n}\right){% endequation %} כלשהי (שמורכבת מנוסחה לוגית {% equation %}\phi{% endequation %} ומשמות-{% equation %}P{% endequation %} {% equation %}\tau_{1},\ldots\tau_{n}{% endequation %} שהוצבו בתוך המשתנים החופשיים שלה) מתקיימת עבור {% equation %}\mathcal{M}\left[G\right]{% endequation %} <strong>כלשהו</strong> (כלומר {% equation %}\phi\left(\tau_{1}^{G},\ldots,\tau_{n}^{G}\right){% endequation %} הוא בעל ערך "אמת"), אז ה"סיבה" לכך שהנוסחה התקיימה היא איבר אחד ויחיד {% equation %}p\in G{% endequation %}. מה זאת אומרת? זה אומר ש<strong>לכל אידאל גנרי</strong> {% equation %}G^{\prime}{% endequation %}, אם {% equation %}p\in G^{\prime}{% endequation %} אז {% equation %}\phi\left(\tau_{1}^{G^{\prime}},\ldots,\tau_{n}^{G^{\prime}}\right){% endequation %}. מתקיימת. על סיטואציה כזו אמרנו ש-{% equation %}p{% endequation %} <strong>כופה</strong> את {% equation %}\phi\left(\tau_{1},\ldots,\tau_{n}\right){% endequation %} וסימנו את זה בתור {% equation %}p\Vdash\phi\left(\tau_{1},\ldots,\tau_{n}\right){% endequation %}.

אז שוב, כדי לחדד, הנה המשפט שאנחנו רוצים להוכיח: שעבור אידאל גנרי {% equation %}G{% endequation %} מתקיים {% equation %}\mathcal{M}\left[G\right]\models\phi\left(\tau_{1}^{G},\ldots,\tau_{n}^{G}\right){% endequation %} אם ורק אם קיים {% equation %}p\in G{% endequation %} כך ש- {% equation %}p\Vdash\phi\left(\tau_{1},\ldots,\tau_{n}\right){% endequation %}.

עד כה, מה שעשינו היה להוכיח את המשפט עבור {% equation %}\phi{% endequation %} שהיא הנוסחה {% equation %}x_{1}=x_{2}{% endequation %}. מן הסתם לא אחזור על כל ההוכחה, אבל <strong>כן אחזור</strong> בקצרה על החלקים ממנה שיהיו רלוונטיים אלינו כי ההוכחה הכללית דומה להם מאוד, רק שאפשר לנפנף בידיים יותר בקלות.

הרעיון הבסיסי הוא לבנות במפורש את ה<strong>יחס</strong> {% equation %}p\Vdash\phi\left(\tau_{1},\ldots,\tau_{n}\right){% endequation %} בעזרת אוסף של קבוצות. יחס כזה הוא אוסף של {% equation %}n+1{% endequation %}-יות, {% equation %}\left(p,\tau_{1},\ldots,\tau_{n}\right){% endequation %}. עכשיו, על שמות ה-{% equation %}P{% endequation %} מוגדרת באופן טבעי היררכייה: כשבנינו אותם, עשינו את זה באמצעות סדרה של קבוצות {% equation %}N_{0},N_{1},N_{2},\ldots{% endequation %} שמאונדקסת על ידי כל הסודרים שיש ב-{% equation %}\mathcal{M}{% endequation %}, כך שהאיברים של כל שם-{% equation %}P{% endequation %} נבנים בעזרת שמות-{% equation %}P{% endequation %} קדומים יותר בהיררכייה. אז עכשיו אנחנו מגדירים {% equation %}\mathcal{F}_{\alpha}^{\phi}{% endequation %} עבור סודר {% equation %}\alpha\in\mathcal{M}{% endequation %} בתור אוסף כל ה-{% equation %}n+1{% endequation %}-יות {% equation %}\left(p,\tau_{1},\ldots,\tau_{n}\right){% endequation %} עבורן {% equation %}\tau_{1},\ldots,\tau_{n}{% endequation %} כולם שייכים ל-{% equation %}N_{\alpha}{% endequation %}, והן מקיימות <strong>תכונה מעניינת</strong> שתלויה ב-{% equation %}\phi{% endequation %} ואיכשהו תוביל לכך שה-{% equation %}n+1{% endequation %}-יות הללו אכן מקודדות את {% equation %}p\Vdash\phi\left(\tau_{1},\ldots,\tau_{n}\right){% endequation %}.

בפוסט הקודם ראינו {% equation %}\mathcal{F}{% endequation %} כאלו עבור יחס השוויון, וה"תכונה מעניינת" המדוברת הייתה מסובכת למדי. למזלנו, הפעם התכונה תהיה פשוטה הרבה יותר כי יש לנו בסיס אינדוקטיבי להסתמך עליו.

קדימה לעבודה.

<h2>אנו נזכרים איך בונים נוסחאות ואיך הוכחנו את המשפט היסודי בפעם הקודמת</h2>

מה זו בעצם "נוסחה"? ראינו את זה בסדרת הפוסטים הזו, אבל למה לא לחזור על זה שוב. אני מדבר פה על נוסחאות בהקשר הספציפי של תורת הקבוצות, כי בלוגיקה מסדר ראשון כללית זה מושג יותר מורכב.

נוסחה בנויה מ<strong>משתנים</strong> {% equation %}x_{1},x_{2},x_{3},\ldots{% endequation %} ומכל מני סימנים לוגיים שתכף נראה. היא תמיד תהיה בסופו של דבר סדרה סופית של סימבולים, אבל עם מבנה בעל משמעות מסוים. שני סוגי הנוסחאות הפשוטים ביותר הם {% equation %}x_{1}=x_{2}{% endequation %} ו-{% equation %}x_{1}\in x_{2}{% endequation %}; הנוסחאות הללו נקראות <strong>נוסחאות אטומיות</strong>. כל נוסחה שאינה אטומית נבנית מתוך נוסחאות פשוטות ביותר {% equation %}\varphi,\psi{% endequation %} באופן הבא: גם {% equation %}\neg\psi{% endequation %} היא נוסחה (שמשמעותה <strong>שלילה</strong> של {% equation %}\psi{% endequation %}), וגם {% equation %}\varphi\to\psi{% endequation %} היא נוסחה (שמשמעותה ש-{% equation %}\varphi{% endequation %} <strong>גוררת לוגית</strong> את {% equation %}\psi{% endequation %}), וגם {% equation %}\forall x\psi{% endequation %} היא נוסחה, לכל משתנה {% equation %}x{% endequation %} (שמשמעותה שלכל ערך שנציב ב-{% equation %}x{% endequation %}, הנוסחה {% equation %}\psi{% endequation %} תתקיים).

יש עוד סימנים לוגיים: למשל {% equation %}\wedge{% endequation %} שמייצג "וגם" ו-{% equation %}\exists{% endequation %} שמייצג "קיים", אבל אפשר לבנות להן נוסחאות שקולות עם הסימנים שכבר ראינו, ולכן כדי לשמור על פשטות אנחנו מסתפקים במה שכבר הצגנו. יש גם עניין עם סוגריים ו"קריאה יחידה" שאני משמיט את הדיבור עליו לגמרי כדי לא לסבך בצורה מיותרת כי בסוף יוצא מזה שמה שאני עושה כרגע הוא בסדר גמור.

עכשיו אפשר להגדיר את הקבוצות {% equation %}\mathcal{F}_{\alpha}^{\phi}{% endequation %} שלנו. עבור {% equation %}\phi{% endequation %} שהוא {% equation %}x_{1}=x_{2}{% endequation %} הגדרנו את זה בפוסט הקודם וקראתי להגדרה <strong>תכונה מעניינת</strong> שהייתה גם מסובכת למדי. עבור יתר המקרים המצב פשוט יותר. אני אסמן את המשתנים החופשיים שמופיעים ב-{% equation %}\phi{% endequation %} בתור {% equation %}x_{1},\ldots,x_{n}{% endequation %}, והאיברים של {% equation %}\mathcal{F}_{\alpha}^{\phi}{% endequation %} יהיו אוסף של {% equation %}n+1{% endequation %}-יות {% equation %}\left(p,\tau_{1},\ldots,\tau_{n}\right){% endequation %} כך ש-{% equation %}p\in P{% endequation %} וכל {% equation %}\tau_{i}{% endequation %} הוא שם-{% equation %}P{% endequation %} מתוך {% equation %}N_{\alpha}{% endequation %}, כך ש-{% equation %}\left(p,\tau_{1},\ldots,\tau_{n}\right){% endequation %} מקיים את התנאי הבא שתלוי במבנה של {% equation %}\phi{% endequation %}:

<ul> <li>אם {% equation %}\phi{% endequation %} מהצורה {% equation %}x_{1}\in x_{2}{% endequation %} אז {% equation %}\left\{ q\in P\ |\ \exists\left(\sigma,q\right)\in\tau_{2}:q\Vdash\tau_{1}=\sigma\right\} {% endequation %} היא <strong>צפופה</strong> מעל {% equation %}p{% endequation %}.</li>


<li>אם {% equation %}\phi{% endequation %} מהצורה {% equation %}\neg\psi{% endequation %} אז <strong>אף הרחבה</strong> של {% equation %}p{% endequation %} לא כופה את {% equation %}\psi\left(\tau_{1},\ldots,\tau_{n}\right){% endequation %}.</li>


<li>אם {% equation %}\phi{% endequation %} מהצורה {% equation %}\psi_{1}\to\psi_{2}{% endequation %} אז כל הרחבה של {% equation %}p{% endequation %} שכופה את {% equation %}\psi_{1}\left(\tau_{1},\ldots,\tau_{n}\right){% endequation %} היא בעלת הרחבה שכופה את {% equation %}\psi_{2}\left(\tau_{1},\ldots,\tau_{n}\right){% endequation %}.</li>


<li>אם {% equation %}\phi{% endequation %} מהצורה {% equation %}\forall x\psi{% endequation %} אז לכל שם-{% equation %}P{% endequation %} {% equation %}\tau{% endequation %}, קבוצת ה-{% equation %}q{% endequation %}-ים שכופים את {% equation %}\psi\left(\tau,\tau_{1},\ldots,\tau_{n}\right){% endequation %} היא <strong>צפופה</strong> מעל {% equation %}p{% endequation %}.</li>

</ul>

יש תחושה של קשר עמום כלשהו בין המבנה של {% equation %}\phi{% endequation %} ובין התנאי שמגדירים, אבל בלי להיכנס להוכחה לא יהיה ברור איך הקשר הזה עובד. אז בואו נדבר על ההוכחה.

עכשיו, איך הלכה ההוכחה עבור {% equation %}x_{1}=x_{2}{% endequation %}? לב ההוכחה היה להגדיר קבוצה {% equation %}A\subseteq P{% endequation %} ולהראות (בערך, אני קצת מרמה) ש-{% equation %}\tau_{1}^{G}=\tau_{2}^{G}{% endequation %} גורר ש-{% equation %}G\subseteq A{% endequation %} ואילו אם עבור {% equation %}p\in G{% endequation %} כלשהו, כל ההרחבות של {% equation %}p{% endequation %} שייכות ל-{% equation %}A{% endequation %}, אז {% equation %}\tau_{1}^{G}=\tau_{2}^{G}{% endequation %}. ההגדרה של {% equation %}A{% endequation %} הזו הייתה קצת מורכבת ונבעה מאופי <strong>התכונה המעניינת</strong> שהגדירה את ה-{% equation %}\mathcal{F}_{\alpha}{% endequation %} עבור הפסוק {% equation %}x_{1}=x_{2}{% endequation %}; עכשיו גם נגדיר קבוצה {% equation %}A{% endequation %} כזו עבור הפסוק {% equation %}\phi{% endequation %} שלנו אבל היא תהיה פשוטה יותר.

אז אנחנו מגדירים את {% equation %}A{% endequation %} להיות קבוצת כל ה-{% equation %}q\in P{% endequation %} אשר מקיימים:

<ul> <li>אם {% equation %}\phi{% endequation %} מהצורה {% equation %}x_{1}\in x_{2}{% endequation %} אז קיים {% equation %}\left(\sigma,q^{\prime}\right)\in\tau_{2}{% endequation %} כך ש-{% equation %}q\subseteq q^{\prime}{% endequation %} ו-{% equation %}q^{\prime}{% endequation %} כופה את {% equation %}\tau_{1}=\sigma{% endequation %}.</li>


<li>אם {% equation %}\phi{% endequation %} מהצורה {% equation %}\neg\psi{% endequation %} אז {% equation %}q{% endequation %} אינו כופה את {% equation %}\psi\left(\tau_{1},\ldots,\tau_{n}\right){% endequation %}</li>


<li>אם {% equation %}\phi{% endequation %} מהצורה {% equation %}\psi_{1}\to\psi_{2}{% endequation %} אז או ש-{% equation %}q{% endequation %} לא כופה את {% equation %}\psi_{1}\left(\tau_{1},\ldots,\tau_{n}\right){% endequation %} או שיש ל-{% equation %}q{% endequation %} הרחבה שכופה את {% equation %}\psi_{2}\left(\tau_{1},\ldots,\tau_{n}\right){% endequation %}.</li>


<li>אם {% equation %}\phi{% endequation %} מהצורה {% equation %}\forall x\psi{% endequation %} אז לכל שם-{% equation %}P{% endequation %} {% equation %}\tau{% endequation %}, קיימת הרחבה של {% equation %}q{% endequation %} שכופה את {% equation %}\psi\left(\tau,\tau_{1},\ldots,\tau_{n}\right){% endequation %}.</li>

</ul>

ההגדרות הללו של שייכות ל-{% equation %}A{% endequation %} דומות כמובן להגדרה של {% equation %}\mathcal{F}_{\alpha}^{\phi}{% endequation %} שראינו קודם. זה קרה גם בפוסט הקודם: ראינו שם שהתנאי של שייכות ל-{% equation %}\mathcal{F}_{\alpha}{% endequation %} בעצם אומר "לכל הרחבה {% equation %}q{% endequation %} של {% equation %}p{% endequation %}, מתקיים ש-{% equation %}q\in A{% endequation %}". זה קורה גם עכשיו: {% equation %}\left(p,\tau_{1},\ldots,\tau_{n}\right)\in\mathcal{F}_{\alpha}^{\phi}{% endequation %} אם ורק אם כל הרחבה של {% equation %}p{% endequation %} שייכת ל-{% equation %}A{% endequation %}. בואו נראה את זה, בזהירות.

ראשית, המקרה של {% equation %}x_{1}\in x_{2}{% endequation %}. אם {% equation %}\left(p,\tau_{1},\tau_{2}\right)\in\mathcal{F}_{\alpha}^{\phi}{% endequation %} אז על פי הגדרה הקבוצה {% equation %}\left\{ q\in P\ |\ \exists\left(\sigma,q\right)\in\tau_{2}:q\Vdash\tau_{1}=\sigma\right\} {% endequation %} היא צפופה מעל {% equation %}p{% endequation %}. המשמעות של "צפופה" היא שלכל הרחבה של {% equation %}p{% endequation %} קיימת הרחבה בתוך הקבוצה הזו. אני רוצה להוכיח שכל הרחבה של {% equation %}p{% endequation %} שייכת ל-{% equation %}A{% endequation %}, אז בואו ניקח הרחבה {% equation %}p\subseteq q{% endequation %} שכזו. על פי הגדרת הצפיפות, קיימת ל-{% equation %}q{% endequation %} הרחבה {% equation %}q\subseteq q^{\prime}{% endequation %} בתוך הקבוצה, כלומר קיימים {% equation %}\left(\sigma,q^{\prime}\right)\in\tau_{2}{% endequation %} כך ש-{% equation %}q^{\prime}\Vdash\tau_{1}=\sigma{% endequation %}. זה בדיוק עונה להגדרה של {% equation %}A{% endequation %} (זה כיוון אחד, אבל השני עובד באותה צורה).

עכשיו למקרה של {% equation %}\neg\psi\left(\tau_{1},\ldots,\tau_{n}\right){% endequation %}. אם {% equation %}\left(p,\tau_{1},\ldots,\tau_{n}\right)\in\mathcal{F}_{\alpha}^{\phi}{% endequation %} אז אף הרחבה של {% equation %}p{% endequation %} לא כופה את {% equation %}\psi\left(\tau_{1},\ldots,\tau_{n}\right){% endequation %}. אם ניקח הרחבה {% equation %}p\subseteq q{% endequation %} כזו, מכיוון שהיא לא כופה את {% equation %}\psi\left(\tau_{1},\ldots,\tau_{n}\right){% endequation %} אז {% equation %}q\in A{% endequation %}. זה היה פשוט, מה? אותו דבר קורה גם במקרה של {% equation %}\psi_{1}\to\psi_{2}{% endequation %}. אבל המקרה של {% equation %}\forall x\psi{% endequation %} שוב מערב צפיפות אז בואו נראה אותו במפורש.

אם כן, אני מניח ש-{% equation %}\left(p,\tau_{1},\ldots,\tau_{n}\right)\in\mathcal{F}_{\alpha}^{\phi}{% endequation %} ולוקח הרחבה {% equation %}p\subseteq q{% endequation %}. עכשיו, בהינתן שם {% equation %}\tau{% endequation %} אנחנו רוצים למצוא הרחבה של {% equation %}q{% endequation %} שכופה את {% equation %}\psi\left(\tau,\tau_{1},\ldots,\tau_{n}\right){% endequation %}. אנחנו משתמשים בכך שקבוצת כל האיברים שכופים את {% equation %}\psi\left(\tau,\tau_{1},\ldots,\tau_{n}\right){% endequation %} היא <strong>צפופה</strong> מעל {% equation %}p{% endequation %}, כלומר לכל הרחבה של {% equation %}p{% endequation %} (ובפרט {% equation %}q{% endequation %}) יש הרחבה ששייכת לקבוצה הזו - בדיוק מה שאנחנו צריכים. זה האופן שבו מושג ה"צפיפות" משרת אותנו.

אוקיי, אז אם לסכם - היה די קל להראות ש-{% equation %}\left(p,\tau_{1},\ldots,\tau_{n}\right)\in\mathcal{F}_{\alpha}^{\phi}{% endequation %} אם ורק אם כל הרחבה של {% equation %}p{% endequation %} שייכת ל-{% equation %}A{% endequation %}. עכשיו, כמו בהוכחה של הפוסט הקודם, {% equation %}A{% endequation %} איכשהו צריכה לעזור לנו לסיים את הוכחת המשפט. זה קורה עם שתי הטענות הבאות:

<ul> <li>אם {% equation %}\mathcal{M}\left[G\right]\models\phi\left(\tau_{1}^{G},\ldots,\tau_{n}^{G}\right){% endequation %} אז {% equation %}G\subseteq A{% endequation %}</li>


<li>אם עבור {% equation %}p\in G{% endequation %} כלשהו כל הרחבה של {% equation %}p{% endequation %} שייכת ל-{% equation %}A{% endequation %} אז {% equation %}\mathcal{M}\left[G\right]\models\phi\left(\tau_{1}^{G},\ldots,\tau_{n}^{G}\right){% endequation %}</li>

</ul>

עבור שוויון השתמשנו באותן שתי טענות בצורה קצת שונה - במקום {% equation %}\mathcal{M}\left[G\right]\models\phi\left(\tau_{1}^{G},\ldots,\tau_{n}^{G}\right){% endequation %} היה לנו {% equation %}\tau_{1}^{G}\subseteq\tau_{2}^{G}{% endequation %} ואותו הדבר גם בכיוון השני עבור {% equation %}A{% endequation %} אחרת ואז איכשהו שילבנו את שני אלו. בשלב הזה אפשר לנפנף בידיים ולהגיד שכל מה שנעשה עכשיו הוא בערך כמו קודם (זה מה שהספר עושה) אבל אני לא מרגיש שאני מבין מה הולך פה מספיק טוב, אז אני אנסה להוכיח הכל פורמלית ככל הניתן. וזה אומר שיהיו שני שלבים, כמקודם: ראשית נראה איך שתי טענות העזר מוכיחות את המשפט; ושנית נראה איך מוכיחים את טענות העזר.

<h2>איך טענות העזר מוכיחות לנו את המשפט היסודי</h2>

יש שתי טענות מרכזיות שצריך להוכיח, עבור נוסחה {% equation %}\phi{% endequation %} ושמות {% equation %}\tau_{1},\ldots,\tau_{n}{% endequation %}:

<ul> <li>עבור אידאל גנרי {% equation %}G{% endequation %} מתקיים {% equation %}\mathcal{M}\left[G\right]\models\phi\left(\tau_{1}^{G},\ldots,\tau_{n}^{G}\right){% endequation %} אם ורק אם קיים {% equation %}p\in G{% endequation %} כך ש- {% equation %}p\Vdash\phi\left(\tau_{1},\ldots,\tau_{n}\right){% endequation %}.</li>


<li>{% equation %}\left(p,\tau_{1},\ldots,\tau_{n}\right)\in\mathcal{F}_{\alpha}^{\phi}{% endequation %} אם ורק אם {% equation %}p\Vdash\phi\left(\tau_{1},\ldots,\tau_{n}\right){% endequation %}</li>

</ul>

בטענה הראשון הכיוון של ה"אם" טריוויאלי (זו המשמעות של כפיה) והחלק המעניין הוא להראות שאם {% equation %}\mathcal{M}\left[G\right]\models\phi\left(\tau_{1}^{G},\ldots,\tau_{n}^{G}\right){% endequation %} אז קיים {% equation %}p\in G{% endequation %} שכופה את {% equation %}\phi\left(\tau_{1},\ldots,\tau_{n}\right){% endequation %}. עכשיו, בזכות טענת העזר הראשונה, {% equation %}\mathcal{M}\left[G\right]\models\phi\left(\tau_{1}^{G},\ldots,\tau_{n}^{G}\right){% endequation %} מלמד אותנו ש-{% equation %}G\subseteq A{% endequation %}. טענת עזר מהפוסט הקודם שאין צורך להוכיח מחדש כי אני משתמש בה כמות שהיא אומרת שאם {% equation %}G\subseteq A\in\mathcal{M}{% endequation %} אז קיים {% equation %}p{% endequation %} כך שכל הרחבה של {% equation %}p{% endequation %} שייכת ל-{% equation %}A{% endequation %}. יחד עם טענת העזר השניה זה מראה לנו שלכל {% equation %}G^{\prime}{% endequation %} כך ש-{% equation %}p\in G^{\prime}{% endequation %} יתקיים {% equation %}\mathcal{M}\left[G^{\prime}\right]\models\phi\left(\tau_{1}^{G^{\prime}},\ldots,\tau_{n}^{G^{\prime}}\right){% endequation %}, וזו בדיוק המשמעות של לומר ש-{% equation %}p{% endequation %} כופה את {% equation %}\left(\tau_{1},\ldots,\tau_{n}\right){% endequation %}.

הדבר היחיד שחסר לנו בשביל הטיעון שבפסקה הקודמת הוא להראות ש-{% equation %}A\in\mathcal{M}{% endequation %}. זה מצריך אותנו לחזור להגדרות השונות והמשונות של {% equation %}A{% endequation %} ולשאול את עצמנו האם יש משהו שמסובך לבנות במסגרת {% equation %}\mathcal{M}{% endequation %} - מסגרת שכזכור מקיימת את ZFC ולכן את כל הדרכים הרגילות שבהן אנו בונים קבוצות. התשובה, בנפנוף ידיים, היא שהכל פשוט - אבל אנחנו צריכים להסתמך על כך שכבר הראינו שכפיה שקולה לשייכות ל-{% equation %}\mathcal{F}_{\beta}^{\psi}{% endequation %} עבור נוסחאות {% equation %}\psi{% endequation %} פשוטות יותר מ-{% equation %}\phi{% endequation %} (כלומר, כאלו שמרכיבות את {% equation %}\phi{% endequation %}) ו/או עבור סודרים {% equation %}\beta{% endequation %} שהם קטנים מ-{% equation %}\alpha{% endequation %}. זו הנחת אינדוקציה סטנדרטית ואין איתה בעיה.

זה סיים את הוכחת הטענה הראשונה, אבל אנחנו זקוקים לשניה - ובדיוק ראינו למה אנחנו זקוקים לה, כדי שנוכל להשתכנע ש-{% equation %}A\in\mathcal{M}{% endequation %}.

נתחיל עם להניח ש-{% equation %}p\Vdash\phi\left(\tau_{1},\ldots,\tau_{n}\right){% endequation %} ונוכיח מתוך זה ש-{% equation %}\left(p,\tau_{1},\ldots,\tau_{n}\right)\in\mathcal{F}_{\alpha}^{\phi}{% endequation %}. כבר הוכחתי קודם ששייכות כזו ל-{% equation %}\mathcal{F}_{\alpha}^{\phi}{% endequation %} פירושה "לכל הרחבה {% equation %}q{% endequation %} של {% equation %}p{% endequation %}, מתקיים ש-{% equation %}q\in A{% endequation %}". עכשיו משתמשים בטריק: אנחנו יודעים שקיים אידאל גנרי {% equation %}G{% endequation %} כך ש-{% equation %}q\in G{% endequation %} כי אפשר לבנות אידאל גנרי שמכיל איבר ספציפי נתון (הוכחנו את זה כשהתחלנו לדבר על אידאלים גנריים). האידאל הזה יכיל את {% equation %}p{% endequation %} שהרי {% equation %}p\subseteq q{% endequation %}, ומכיוון ש-{% equation %}p{% endequation %} כופה דברים, נקבל {% equation %}\mathcal{M}\left[G\right]\models\phi\left(\tau_{1}^{G},\ldots,\tau_{n}^{G}\right){% endequation %}, מה שלפי טענת העזר הראשונה מוכיח {% equation %}G\subseteq A{% endequation %} ולכן {% equation %}q\in G\subseteq A{% endequation %} שייך ל-{% equation %}A{% endequation %} וזה מה שרצינו.

נשאר רק הכיוון השני! זה שבו מניחים {% equation %}\left(p,\tau_{1},\ldots,\tau_{n}\right)\in\mathcal{F}_{\alpha}^{\phi}{% endequation %} ומוכיחים {% equation %}p\Vdash\phi\left(\tau_{1},\ldots,\tau_{n}\right){% endequation %}. כלומר, אנחנו לוקחים אידאל גנרי {% equation %}G{% endequation %} כך ש-{% equation %}p\in G{% endequation %} וצריכים להראות {% equation %}\mathcal{M}\left[G\right]\models\phi\left(\tau_{1}^{G},\ldots,\tau_{n}^{G}\right){% endequation %}. טענת העזר השניה אומרית שזה קורה אם כל הרחבה של {% equation %}p{% endequation %} שייכת ל-{% equation %}A{% endequation %}, וזה... כמו שראינו קודם... שקול בדיוק אל {% equation %}\left(p,\tau_{1},\ldots,\tau_{n}\right)\in\mathcal{F}_{\alpha}^{\phi}{% endequation %}, אז בעצם אין עוד מה לעשות! סיימנו את הוכחת המשפט היסודי! בהינתן הוכחה לטענות העזר, שלא הוכחתי עדיין.

<h2>ההוכחה לטענות העזר שלא הוכחתי עדיין</h2>

אוקיי, הנה טענות העזר שוב:

<ul> <li>אם {% equation %}\mathcal{M}\left[G\right]\models\phi\left(\tau_{1}^{G},\ldots,\tau_{n}^{G}\right){% endequation %} אז {% equation %}G\subseteq A{% endequation %}</li>


<li>אם עבור {% equation %}p\in G{% endequation %} כלשהו כל הרחבה של {% equation %}p{% endequation %} שייכת ל-{% equation %}A{% endequation %} אז {% equation %}\mathcal{M}\left[G\right]\models\phi\left(\tau_{1}^{G},\ldots,\tau_{n}^{G}\right){% endequation %}</li>

</ul>

נתחיל מהטענה הראשונה: אנחנו מניחים שב-{% equation %}\mathcal{M}\left[G\right]{% endequation %} מתקיים הפסוק {% equation %}\phi\left(\tau_{1}^{G},\ldots,\tau_{n}^{G}\right){% endequation %} ורוצים להשתמש בזה כדי להראות שעבור {% equation %}q\in G{% endequation %} כלשהו מתקיים {% equation %}q\in A{% endequation %}. זה תלוי, מן הסתם, בהגדרה הספציפית של {% equation %}A{% endequation %} שתלויה בתורה במבנה של {% equation %}\phi{% endequation %}. מה שאומר שפתאום ההוכחה הקלילה שלנו הפכה להתעסקות ב<strong>ארבעה</strong> מקרים שונים.

במקרה הראשון {% equation %}q\in A{% endequation %} אם:

<ul> <li>אם {% equation %}\phi{% endequation %} מהצורה {% equation %}x_{1}\in x_{2}{% endequation %} אז קיים {% equation %}\left(\sigma,q^{\prime}\right)\in\tau_{2}{% endequation %} כך ש-{% equation %}q\subseteq q^{\prime}{% endequation %} ו-{% equation %}q^{\prime}{% endequation %} כופה את {% equation %}\tau_{1}=\sigma{% endequation %}.</li>

</ul>

הידע שיש לנו הוא ש-{% equation %}\mathcal{M}\left[G\right]\models\phi\left(\tau_{1}^{G},\ldots,\tau_{n}^{G}\right){% endequation %}, כלומר בהקשר של {% equation %}\phi{% endequation %} הזו, {% equation %}\tau_{1}^{G}\in\tau_{2}^{G}{% endequation %}. המשמעות של השייכות הזו היא שקיימים {% equation %}\left(\sigma,q_{1}\right)\in\tau_{2}{% endequation %} כך ש-{% equation %}\tau_{1}^{G}=\sigma^{G}{% endequation %} ועכשיו קורה <strong>קסם</strong>! אנחנו יכולים להשתמש במשפט שהוכחנו בפוסט הקודם עבור שוויון ולהסיק שאם קורה {% equation %}\tau_{1}^{G}=\sigma^{G}{% endequation %}, אז קיים {% equation %}q_{2}\in G{% endequation %} שכופה את {% equation %}\tau_{1}=\sigma{% endequation %}. אפשר עכשיו לקחת הרחבה משותפת {% equation %}q_{1},q_{2}\subseteq q^{\prime}{% endequation %} ולקבל את ה-{% equation %}q^{\prime}{% endequation %} שרצינו.

הטכניקה הזו של "הרחבה משותפת" עדיין קצת מבלבלת אפילו אותי, אז הנה תזכורת למה זה עובד כאן: ראשית, {% equation %}G{% endequation %} אידאל ולכן לכל שני איברים שלו יש הרחבה משותפת (אצלנו האיברים הללו הם {% equation %}q_{1},q_{2}{% endequation %}). שנית, על פי הבניה של שמות-{% equation %}P{% endequation %}, אם {% equation %}\left(\sigma,q_{1}\right)\in\tau_{2}{% endequation %} אז {% equation %}\left(\sigma,q^{\prime}\right)\in\tau_{2}{% endequation %} לכל הרחבה {% equation %}q^{\prime}{% endequation %} של {% equation %}q_{1}{% endequation %} ולכן בפרט לזו שבנינו; ולבסוף, אם {% equation %}q_{2}{% endequation %} כופה <strong>משהו</strong>, גם {% equation %}q^{\prime}{% endequation %} יכפה אותו, כי אם ניקח אידאל {% equation %}G^{\prime}{% endequation %} כלשהו כך ש-{% equation %}q^{\prime}\in G^{\prime}{% endequation %} אז בגלל הסגירות כלפי מטה של אידאלים גם {% equation %}q_{2}\in G^{\prime}{% endequation %} והקיום שלו באידאל מבטיח שה<strong>משהו</strong> יתקיים עבור {% equation %}G^{\prime}{% endequation %}. את כל זה ראינו גם בפוסט הקודם ולפחות עבורי זה מרגיש קצת יותר טבעי עכשיו למרות שאני עדיין טובע בפרטים.

האם אני מרגיש בטוח בעצמי מספיק כדי לדלג על הוכחה טרחנית מפורשת של שאר המקרים? לא! למה להפסיק עכשיו, כשזה סוף סוף נהיה קל?

אז במקרה השני {% equation %}q\in A{% endequation %} אם:

<ul> <li>אם {% equation %}\phi{% endequation %} מהצורה {% equation %}\neg\psi{% endequation %} אז {% equation %}q{% endequation %} אינו כופה את {% equation %}\psi\left(\tau_{1},\ldots,\tau_{n}\right){% endequation %}</li>

</ul>

הידע שיש לנו הוא ש-{% equation %}\mathcal{M}\left[G\right]\models\neg\psi\left(\tau_{1}^{G},\ldots,\tau_{n}^{G}\right){% endequation %}, כלומר אנחנו יודעים ש<strong>לא מתקיים</strong> {% equation %}\neg\psi\left(\tau_{1}^{G},\ldots,\tau_{n}^{G}\right){% endequation %}. עכשיו, אם {% equation %}q{% endequation %} <strong>כן</strong> כופה את {% equation %}\psi\left(\tau_{1},\ldots,\tau_{n}\right){% endequation %} אז מכיוון ש-{% equation %}q\in G{% endequation %} זה אומר ש<strong>כן מתקיים</strong> {% equation %}\psi\left(\tau_{1}^{G},\ldots,\tau_{n}^{G}\right){% endequation %}, וזו סתירה. היי, זה היה קל! קל מדי...? אם כן, כנראה יעירו לי בתגובות עוד כמה שנים טובות כשכבר לא אזכור כלום ממה שהלך פה.

קדימה למקרה השלישי! {% equation %}q\in A{% endequation %} אם:

<ul> <li>אם {% equation %}\phi{% endequation %} מהצורה {% equation %}\psi_{1}\to\psi_{2}{% endequation %} אז או ש-{% equation %}q{% endequation %} לא כופה את {% equation %}\psi_{1}\left(\tau_{1},\ldots,\tau_{n}\right){% endequation %} או שיש ל-{% equation %}q{% endequation %} הרחבה שכופה את {% equation %}\psi_{2}\left(\tau_{1},\ldots,\tau_{n}\right){% endequation %}.</li>

</ul>

הידע שיש לנו הוא ש-{% equation %}\mathcal{M}\left[G\right]\models\psi_{1}\to\psi_{2}{% endequation %}, כלומר אנחנו יודעים שמתקיים אחד משניים: או ש-{% equation %}\psi_{1}{% endequation %} לא מתקיים, או ש-{% equation %}\psi_{2}{% endequation %} כן מתקיים.

הדרך היחידה שבה {% equation %}q{% endequation %} לא יקיים את התנאי של {% equation %}A{% endequation %} הוא אם {% equation %}q{% endequation %} <strong>כן יכפה</strong> את {% equation %}\psi_{1}{% endequation %} אבל <strong>לא תהיה</strong> לו הרחבה שכופה את {% equation %}\psi_{2}{% endequation %}. מכיוון ש-{% equation %}q{% endequation %} כופה את {% equation %}\psi_{1}{% endequation %} אז {% equation %}\psi_{1}{% endequation %} מתקיים; ולכן מסיקים מ-{% equation %}\mathcal{M}\left[G\right]\models\psi_{1}\to\psi_{2}{% endequation %} ש-{% equation %}\psi_{2}{% endequation %} כן מתקיים. כאן נכנסת לפעולה הנחת האינדוקציה: מכיוון ש-{% equation %}\psi_{2}{% endequation %} היא נוסחה פשוטה יותר מ-{% equation %}\phi{% endequation %} אפשר להניח שכבר הוכחנו עבורה את המשפט המרכזי. כלומר, מכך ש-{% equation %}\mathcal{M}\left[G\right]\models\psi_{2}{% endequation %} אפשר להסיק שקיים ב-{% equation %}G{% endequation %} איבר שכופה את {% equation %}\psi_{2}{% endequation %}, ואז ניקח הרחבה משותפת שלו ושל {% equation %}q{% endequation %} ונקבל הרחבה של {% equation %}q{% endequation %} שכופה את {% equation %}\psi_{2}{% endequation %}, מה שמסיים את המקרה הזה.

נשאר רק המקרה האחרון. {% equation %}q\in A{% endequation %} אם:

<ul> <li>אם {% equation %}\phi{% endequation %} מהצורה {% equation %}\forall x\psi{% endequation %} אז לכל שם-{% equation %}P{% endequation %} {% equation %}\tau{% endequation %}, קיימת הרחבה של {% equation %}q{% endequation %} שכופה את {% equation %}\psi\left(\tau,\tau_{1},\ldots,\tau_{n}\right){% endequation %}.</li>

</ul>

הידע שיש לנו הוא ש-{% equation %}\mathcal{M}\left[G\right]\models\forall x\psi\left(x,\tau_{1}^{G},\ldots,\tau_{n}^{G}\right){% endequation %}. מה זה בעצם אומר, פורמלית? אם נסתכל על הנוסחה {% equation %}\forall x\psi\left(x,x_{1},\ldots,x_{n}\right){% endequation %} נראה שיש לה משתנים חופשיים: {% equation %}x_{1},\ldots,x_{n}{% endequation %}. בנוסף יש בה גם משתנים קשורים, כאלו שנופלים תחת כמת - לכל הפחות, {% equation %}x{% endequation %} הוא כזה. עכשיו, בשלב הראשון החלפנו את כל המשתנים החופשיים באיברים קונקרטיים, {% equation %}\tau_{1}^{G},\ldots,\tau_{n}^{G}{% endequation %}. נשאר לחשב את ערך האמת של הפסוק על ידי הצבה של ערכים במשתנים המכומתים. הכתיב {% equation %}\mathcal{M}\left[G\right]\models{% endequation %} בעצם אומר לי שה"עולם" שממנו מגיעים הערכים שאפשר להציב במשתנים הללו הוא {% equation %}\mathcal{M}\left[G\right]{% endequation %}. בפרט, אם {% equation %}\tau{% endequation %} הוא שם-{% equation %}P{% endequation %} כלשהו, אז אם נציב ב-{% equation %}x{% endequation %} את {% equation %}\tau^{G}{% endequation %} מובטח לנו שיתקיים {% equation %}\mathcal{M}\left[G\right]\models\psi\left(\tau^{G},\tau_{1}^{G},\ldots,\tau_{n}^{G}\right){% endequation %}.

עכשיו שוב אפשר להשתמש בהנחת האינדוקציה, כי {% equation %}\psi{% endequation %} פשוט יותר מ-{% equation %}\phi{% endequation %}, ולקבל שקיים איבר ב-{% equation %}G{% endequation %} שכופה את {% equation %}\psi\left(\tau,\tau_{1},\ldots,\tau_{n}\right){% endequation %}, לקחת הרחבה משותפת שלו ושל {% equation %}q{% endequation %}, וסיימנו! היה שווה לעשות את כל הצעדים במפורש כי עכשיו הטכניקה ממש ברורה וקלילה - וממילא כל ההוכחה הזו הייתה פשוטה בהרבה מהסיבוך שהיה לנו עבור השוויון בפוסט הקודם (כי שם לא היו לנו הנחות אינדוקציה פשוטות להסתמך עליהן).

האם סיימנו? לא! כי יש עוד טענת עזר שצריך להוכיח:

<ul> <li>אם עבור {% equation %}p\in G{% endequation %} כלשהו כל הרחבה של {% equation %}p{% endequation %} שייכת ל-{% equation %}A{% endequation %} אז {% equation %}\mathcal{M}\left[G\right]\models\phi\left(\tau_{1}^{G},\ldots,\tau_{n}^{G}\right){% endequation %}</li>

</ul>

גם פה אין מנוס מלפרק למקרים על פי המבנה של {% equation %}\phi{% endequation %}. נקווה שגם זה יהיה קל!

אז שוב, במקרה הראשון, {% equation %}q\in A{% endequation %} אם:

<ul> <li>אם {% equation %}\phi{% endequation %} מהצורה {% equation %}x_{1}\in x_{2}{% endequation %} אז קיים {% equation %}\left(\sigma,q^{\prime}\right)\in\tau_{2}{% endequation %} כך ש-{% equation %}q\subseteq q^{\prime}{% endequation %} ו-{% equation %}q^{\prime}{% endequation %} כופה את {% equation %}\tau_{1}=\sigma{% endequation %}.</li>

</ul>

במקרה הזה אנחנו רוצים להוכיח ש-{% equation %}\tau_{1}^{G}\in\tau_{2}^{G}{% endequation %}. כלומר, שקיים {% equation %}\left(\sigma,q\right)\in\tau_{2}{% endequation %} כך ש-{% equation %}\tau_{1}^{G}=\sigma^{G}{% endequation %}. בשביל זה מספיק למצוא איבר ב-{% equation %}G{% endequation %} שכופה את {% equation %}\tau_{1}=\sigma{% endequation %} עבור {% equation %}\sigma{% endequation %} כלשהו שמופיע ב-{% equation %}\tau_{2}{% endequation %}. לכאורה ההגדרה של {% equation %}A{% endequation %} נותנת לנו איבר כזה, אבל צריך להיזהר פה: לכל הרחבה של {% equation %}p\in G{% endequation %} יש הרחבה נוספת {% equation %}q^{\prime}{% endequation %} שכופה את {% equation %}\tau_{1}=\sigma{% endequation %} עבור {% equation %}\sigma{% endequation %} מתאים, אבל שום דבר לא מבטיח לנו ש-{% equation %}q^{\prime}\in G{% endequation %}. לא בלי טיעון נוסף.

בפוסט הקודם הטיעון הנוסף היה לקחת את קבוצת <strong>כל האיברים</strong> שכופים את מה שאנחנו רוצים, כלומר במקרה שלנו זו הקבוצה

{% equation %}D=\left\{ q^{\prime}\in P\ |\ \exists\left(\sigma,q^{\prime}\right)\in\tau_{2}:q^{\prime}\Vdash\tau_{1}=\sigma\right\} {% endequation %}

בפוסט הקודם האבחנה הייתה ש-{% equation %}D{% endequation %} צפופה מעל איבר של {% equation %}G{% endequation %}, וזה קורה גם כאן: {% equation %}D{% endequation %} צפופה מעל {% equation %}p{% endequation %} כי לכל הרחבה של {% equation %}p{% endequation %}, ההרחבה שייכת ל-{% equation %}A{% endequation %} (ההנחה שלנו) ולכן קיימת לה הרחבה ששייכת ל-{% equation %}D{% endequation %} (כי זו המשמעות של שייכות ל-{% equation %}A{% endequation %} במקרה הזה). הצפיפות הזו עוזרת לנו כי ראינו שאם {% equation %}D\in\mathcal{M}{% endequation %} היא צפופה מעל {% equation %}p\in G{% endequation %} אז {% equation %}G\cap D\ne\emptyset{% endequation %} ולכן אנחנו מקבלים שיש ב-{% equation %}G{% endequation %} איבר שכופה {% equation %}\tau_{1}=\sigma{% endequation %}, כפי שרצינו.

בשביל שכל זה יעבוד צריך שיתקיים {% equation %}D\in\mathcal{M}{% endequation %} מה שדורש שאפשר יהיה לנסח את יחס הכפייה במסגרת {% equation %}\mathcal{M}{% endequation %}. זה <strong>לא</strong> נובע מהנחת אינדוקציה כי {% equation %}\tau_{1}{% endequation %} הוא לא משהו שיש לנו הנחת אינדוקציה עליו, הרי הוא מה שאנחנו מנסים להוכיח עליו דברים עכשיו. אבל למרבה המזל, יחס הכפייה המדובר הוא של {% equation %}\tau_{1}=\sigma{% endequation %}, כלומר של שוויון, שבו טיפלנו בנפרד (ובדם יזע ודמעות...) ולכן אנחנו יודעים כבר שאפשר לנסח אותו במסגרת {% equation %}\mathcal{M}{% endequation %} גם בלי שום הנחת אינדוקציה. זו המחשה יפה של העובדה שלמרות שגם {% equation %}x_{1}=x_{2}{% endequation %} וגם {% equation %}x_{1}\in x_{2}{% endequation %} שניהם פסוקים אטומיים, המקרה של שוויון הוא "יותר בסיסי" עבורנו.

קודם המקרה השני היה קל מאוד. האם גם הפעם? {% equation %}q\in A{% endequation %} אם:

<ul> <li>אם {% equation %}\phi{% endequation %} מהצורה {% equation %}\neg\psi{% endequation %} אז {% equation %}q{% endequation %} אינו כופה את {% equation %}\psi\left(\tau_{1},\ldots,\tau_{n}\right){% endequation %}</li>

</ul>

במקרה הזה אנחנו רוצים להוכיח ש-{% equation %}\mathcal{M}\left[G\right]\models\phi\left(\tau_{1}^{G},\dots,\tau_{n}^{G}\right){% endequation %}, כלומר ש-{% equation %}\mathcal{M}\left[G\right]{% endequation %} <strong>לא</strong> מספקת את {% equation %}\psi\left(\tau_{1}^{G},\ldots,\tau_{n}^{G}\right){% endequation %}. אנחנו יודעים, בעזרת הנחת האינדוקציה, שאם {% equation %}\mathcal{M}\left[G\right]{% endequation %} כן הייתה מספקת אותו אז היה קיים ב-{% equation %}G{% endequation %} איבר שכופה את {% equation %}\psi\left(\tau_{1},\ldots,\tau_{n}\right){% endequation %}. אפשר לקחת הרחבה של האיבר הזה ושל {% equation %}p{% endequation %}, ולקבל הרחבה {% equation %}p\subseteq q{% endequation %} שכופה את {% equation %}\psi\left(\tau_{1},\ldots,\tau_{n}\right){% endequation %}, מה שסותר את ההנחה שכל הרחבה של {% equation %}p{% endequation %} שייכת ל-{% equation %}A{% endequation %}. זה מסיים את המקרה הזה, שבאמת היה קל (ואולי... אני שוב מפספס משהו!)

קדימה אל המקרה השלישי! {% equation %}q\in A{% endequation %} אם:

<ul> <li>אם {% equation %}\phi{% endequation %} מהצורה {% equation %}\psi_{1}\to\psi_{2}{% endequation %} אז או ש-{% equation %}q{% endequation %} לא כופה את {% equation %}\psi_{1}\left(\tau_{1},\ldots,\tau_{n}\right){% endequation %} או שיש ל-{% equation %}q{% endequation %} הרחבה שכופה את {% equation %}\psi_{2}\left(\tau_{1},\ldots,\tau_{n}\right){% endequation %}.</li>

</ul>

כאן כדי להוכיח {% equation %}\mathcal{M}\left[G\right]\models\phi\left(\tau_{1}^{G},\dots,\tau_{n}^{G}\right){% endequation %} מספיק להניח ש-{% equation %}\mathcal{M}\left[G\right]\models\psi_{1}{% endequation %} ולהוכיח ש-{% equation %}\mathcal{M}\left[G\right]\models\psi_{2}{% endequation %}. הפעם נגדיר

{% equation %}D=\left\{ q^{\prime}\in P\ |\ q^{\prime}\Vdash\psi_{2}\left(\tau_{1},\ldots,\tau_{n}\right)\right\} {% endequation %}

ושוב - אם נוכיח ש-{% equation %}D{% endequation %} צפופה מעל {% equation %}p{% endequation %}, סיימנו (הפעם {% equation %}D\in\mathcal{M}{% endequation %} בעזרת הנחת האינדוקציה של המשפט היסודי על {% equation %}\psi_{2}{% endequation %}). אז אנחנו לוקחים הרחבה {% equation %}p\subseteq q{% endequation %} ומראים שיש לה הרחבה ב-{% equation %}D{% endequation %}.

מכך ש-{% equation %}\mathcal{M}\left[G\right]\models\psi_{1}{% endequation %}, על ידי הפעלת הנחת האינדוקציה של המשפט היסודי על {% equation %}\psi_{1}{% endequation %}, אפשר לקבל שיש איבר ב-{% equation %}G{% endequation %} שכופה את {% equation %}\psi_{1}{% endequation %} ולקחת הרחבה משותפת שלו ושל {% equation %}q{% endequation %} שגם תכפה את {% equation %}\psi_{1}{% endequation %} וגם תהיה שייכת ל-{% equation %}A{% endequation %} (כי כל הרחבה של {% equation %}p{% endequation %} שייכת ל-{% equation %}A{% endequation %}). השייכות ל-{% equation %}A{% endequation %}, יחד עם הכפיה של {% equation %}\psi_{1}{% endequation %}, מלמדים אותנו שלאיבר הזה יש הרחבה שכופה את {% equation %}\psi_{2}{% endequation %}, שזה מה שרצינו.

זהו, הגענו למקרה האחרון בכיוון הזה, ולכן גם לשלב האחרון של ההוכחה של המשפט היסודי. {% equation %}q\in A{% endequation %} אם:

<ul> <li>אם {% equation %}\phi{% endequation %} מהצורה {% equation %}\forall x\psi{% endequation %} אז לכל שם-{% equation %}P{% endequation %} {% equation %}\tau{% endequation %}, קיימת הרחבה של {% equation %}q{% endequation %} שכופה את {% equation %}\psi\left(\tau,\tau_{1},\ldots,\tau_{n}\right){% endequation %}.</li>

</ul>

כאן כדי להוכיח {% equation %}\mathcal{M}\left[G\right]\models\phi\left(\tau_{1}^{G},\dots,\tau_{n}^{G}\right){% endequation %} אנחנו צריכים לקחת שם-{% equation %}P{% endequation %} כלשהו {% equation %}\tau{% endequation %} ולהראות ש-{% equation %}\mathcal{M}\left[G\right]\models\psi\left(\tau^{G},\tau_{1}^{G},\dots,\tau_{n}^{G}\right){% endequation %}. ננקוט באותו תעלול שעבד קודם: נגדיר {% equation %}D=\left\{ q\in P\ |\ q\Vdash\psi\left(\tau,\tau_{1},\ldots,\tau_{n}\right)\right\} {% endequation %}; ניקח הרחבה של {% equation %}p{% endequation %}, אנחנו יודעים שהיא ב-{% equation %}A{% endequation %} ולכן עבור {% equation %}\tau{% endequation %} קיימת הרחבה {% equation %}q{% endequation %} שלה שכופה את {% equation %}\psi\left(\tau,\tau_{1},\ldots,\tau_{n}\right){% endequation %}, ולכן שייכת ל-{% equation %}D{% endequation %}, ומכיוון ש-{% equation %}D\in\mathcal{M}{% endequation %} (הנחת האינדוקציה עבור {% equation %}\psi{% endequation %}) נקבל שיש ב-{% equation %}G{% endequation %} איבר של {% equation %}D{% endequation %}, וסיימנו!

<h2>סיכום קצר לפני שממשיכים הלאה</h2>

סיימנו להוכיח את המשפט היסודי! זה דרש פוסט ארוך פחות מאשר ההוכחה של המקרה הפרטי של {% equation %}x_{1}=x_{2}{% endequation %}, והסתמכנו על מה שהלך שם בכמה דרכים שונות - גם באופן ישיר בתוצאה עצמה שהוכחנו (הסקנו מ-{% equation %}\tau_{1}^{G}=\tau_{2}^{G}{% endequation %} שיש איבר שכופה את {% equation %}\tau_{1}=\tau_{2}{% endequation %}), גם על ידי הדמיון בין ההוכחה במקרה הפרטי וההוכחה במקרה הכללי (כל הקטע הזה עם הקבוצות {% equation %}A{% endequation %} ו-{% equation %}D{% endequation %}) וגם על ידי שימוש חוזר בתוצאות העזר שהוכחנו בפעם הקודמת (למשל עם הצפיפות של {% equation %}D{% endequation %} שמובילה לחיתוך לא ריק עם {% equation %}G{% endequation %}). אני מקווה שתוך כדי ההוכחה גם התרגלנו קצת לכוח הגדול של המשפט. עכשיו מגיע הזמן להתחיל לקטוף את הפירות סוף כל סוף; ראשית כל לסיים להוכיח ש-{% equation %}\mathcal{M}\left[G\right]{% endequation %} מקיימת את כל אקסיומות ZFC, ובפרט את אקסיומות ההפרדה, קבוצת החזקה, ההחלפה והבחירה; ולאחר מכן סוף סוף לבצע כפיות קונקרטיות עבור קבוצות {% equation %}P{% endequation %} של תנאי כפייה שבפעם אחת יתנו לנו את השערת הרצף ובפעם אחרת את שלילתה. יהיה כיף. 
